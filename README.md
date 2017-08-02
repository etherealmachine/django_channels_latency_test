# TL;DR: Latency in Django Channels is surprisingly high

I put together a barebones example that echos back JSON messages. Javascript on the page tracks round trip time, as well as time to and from the server. Note that to/from times are calculated using the system clock and will only be accurate running locally.

The round trip time is surprisingly high. I have seen average values as low as 12ms when running on bare metal, but even that seems way to high. I can write a barebones websocket handler that can echo messages in microseconds, so even 10 milliseconds is a lot of overhead being imposed somewhere in the system.

![Example Screenshot](https://raw.githubusercontent.com/etherealmachine/django_channels_latency_test/master/screenshot.png)

```
> sudo docker build .
  ... Successfully built <XYZ>
> sudo docker tag <XYZ> channels_test
> sudo docker-compose up
```
