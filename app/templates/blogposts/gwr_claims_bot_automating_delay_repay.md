# GWR Claims Bot - Automating Delay Repay

## What ?
gwr_claims_bot is a Telegram bot I have built that automates filing delay
compensation claims with GWR (Great Western Railway). You message the bot
([@gwr_claims_bot](https://t.me/gwr_claims_bot)), it stores your details
(encrypted at rest), and it drives the whole claim submission. This is including
solving the reCAPTCHA so you don't have to do it by hand every time your
train is late.

Repo: [gwr_claims_bot](https://github.com/AdrianHRedhe/gwr_claims_bot)

## Demo
<video controls muted playsinline preload="metadata" style="width:100%;border-radius:6px;">
  <source src="/static/videos/gwr_claims_bot_demo.mp4" type="video/mp4">
</video>

## Why ?
A friend of mine recently moved to London to start her work at a satelite
startup. The office is in a town about 40 mins away with a train & the tickets
cost about ~550 pounds / ~7000 SEK. From what she said they were also often
late.

You can get reinbursements if you report a late train, but it is tedious and a
manual process, you also have to have used your card at a train that was
actually late. So she asked me if I could build somethign to simplify the
process for her and her collegues.

## How ?
### Getting updates in
There are two ways updates come in one that polls Telegram's `getUpdates`
endpoint, meant to run on a cron every minute leading to many polls and and
slow replies. OK for testing during development.  

Another which uses a webhook server that Telegram calls directly instead, so
replies are near-instant. This is a FastAPI app which is paired with a
Cloudflare webtunnel so that I can expose only one endpoint from my server to
Cloudflare rather than my network as a whole

### Routing a conversation
Once a message comes in, the bot works out what to do based on where you are in
the flow: no registered user yet -> it prompts registration, registered but no
ticket photo uploaded -> it says that you need to upload one, send `/claim` ->
kick off the automation, anything else -> show the available commands. It's a
simple ordered list of checks rather than a proper state machine, which keeps
it easy to follow for something this size.

### Finding a train worth claiming for
Rather than asking which train you took, the bot scrapes GWR's own live "check
your journey" page itself. Based on the time of day it assumes the commute
direction (into London before 1pm, back out after), and picks the first
upcoming *fast* train (under 30 minutes) from the results. That was the whole
point for my friend and her colleagues `/claim` should just work without anyone
having to remember departure times. Idea is based on the idea that quick
registration is exactly for when you are there and the train is late meaning
that your train is the next train. However for this to be more broad it should
be switched so that the step of registering your standard trip is part of
registration

### Filling in the claim itself
The actual claim is filled in with a headless browser against GWR's delay
repay site: log in, pick "Today", fill in personal details and address,
search the journey (times snap to the site's own 15-minute options, so the
departure time gets rounded down first), pick ticket type/price/smartcard
number, upload the ticket photo, fill in bank details for the payout, and
submit. Every step is written against the site's own labels and buttons
rather than brittle styling-based selectors, which is what makes it survive
GWR tweaking their design. On both success and failure it takes a full-page
screenshot and sends it back over Telegram, so I can actually see what
happened without digging through logs.

### The CAPTCHA
The claim form is protected by a reCAPTCHA, so the bot pulls the challenge
straight off the page, sends it to a solving service, and feeds the answer
back in the same way a person completing it would - so from the page's point
of view a real challenge was just completed.

### Keeping user data safe
Personal details and the ticket photo are the sensitive parts, so both are
kept encrypted at rest, with separate keys for the text and the image - so
rotating or leaking one doesn't automatically compromise the other. Nothing
fancier than that.

## Disclaimer
This bot is for educational purposes. Users are responsible
for ensuring their use complies with GWR's terms of service
and applicable laws. It is an unofficial tool, not affiliated
with or endorsed by Great Western Railway.
