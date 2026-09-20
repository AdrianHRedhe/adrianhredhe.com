# Plantstatus - A houseplant with a kafka pipeline

## What ?
Plantstatus is a small home project that tells me whether my plant needs water
and whether or not it is light where it is at. An ESP32 reads a soil moisture
sensor and a light sensor, and the readings flow through a proper streaming
pipeline into a Grafana dashboard. You can see the live dashboard on the [Plant
Status page](/services/plantstatus).

<img src="/static/images/plantstatus/sensor_in_plant.jpg" alt="The soil moisture and light sensors wired into the actual plant pot" style="width:40%;border-radius:10px;">

## Why ?
I like taking care of my houseplants, it just so happens that most of them
are monsteras or succulents which should not be watered too often. I found
myself thinking, if I had actually watered them or not quite frequently.

But mainly I wanted an excuse to overengineer something, and a friend of mine
just so happened to have a moisture sensor laying around. I know this is not a
valid use case for kafka, but I thought it would be fund to handle it as if it
was.

The project exists to learn kafka hands-on, not because a plant needs a
distributed log. Along the way I also picked up some MicroPython and basic
electronics, neither of which I'd touched before. I also got familiar with how
much of a chore it is to solder.

## How ?
### Architecture
```
ESP32 → HTTP POST → FastAPI → Kafka → consumer → TimescaleDB → Grafana
```

The ESP32 reads both sensors on a loop and POSTs the raw values to a small
FastAPI service. That service owns the Kafka producer and puts each reading
on a topic - it does no storage itself, so it stays thin and fast to
respond to. A separate consumer process subscribes to that topic and writes
every reading into TimescaleDB (Postgres with the timescaledb extension).
Grafana then reads from a continuous aggregate - the readings pre-bucketed
into 10-minute windows - and serves the dashboard, embedded directly on
this site as an iframe.

Splitting ingestion (the API) from storage (the consumer) via Kafka in the
middle means either side can go down without losing data - readings just
queue up on the topic until the consumer is back. Total overkill for a
plant that won't notice a missed sensor reading, but it's exactly the
failure mode you want decoupled in a real system.

### The hardware side
This was the part I found hardest, having never really dealt with
electronics before. A capacitive soil moisture sensor and an LDR light
sensor both feed into the ESP32's ADC pins through a breadboard, with a
resistor on each to pull the readings into a usable range - without them,
both sensors basically just read near the max value regardless of actual
conditions.
<img src="/static/images/plantstatus/in_box.jpg" alt="electronics put in the box" style="width:40%;border-radius:10px;">

The firmware itself is MicroPython: connect to WiFi, read both ADC pins in
a loop, send the raw values as JSON over HTTP, sleep a second, repeat. No
on-device logic beyond that - all the calibration and interpretation
happens downstream, which keeps the ESP32 side trivial to reason about and
easy to iterate on without reflashing constantly.

### Getting it into the plant
Once the wiring was proven out on a breadboard, the sensors moved into the
actual pot.
<img src="/static/images/plantstatus/in_plant.jpg" alt="Box closed and put into the plant" style="width:40%;border-radius:10px;">
