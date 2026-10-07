## Plant Status

An ESP32 reads a soil moisture sensor and a light sensor on my houseplant, and
the readings flow through a small Kafka pipeline into the Grafana dashboard
below. Read more about how it's built in the [blog
post](/blog/plantstatus_a_houseplant_with_a_kafka_pipeline.md).

<div class="wide-embed-outer">
<div class="wide-embed plantstatus-embed">
<iframe src="{{ grafana_url }}" width="100%" height="100%" frameborder="0"></iframe>
</div>
</div>

<style>
.plantstatus-embed {
  /* Fits the Grafana dashboard's two 8-row panels, the collapsed
     "Raw ADC" row and the kiosk footer, so there's no inner scrollbar. */
  height: 720px;
}
</style>
