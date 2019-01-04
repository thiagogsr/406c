# House automation

- Flash a SD card with [Openhabian OS](https://www.openhab.org/docs/installation/openhabian.html)
- After setup the OS, install que MQTT Server
- Change the MQTT host in `openhab2/things/406.things`
- Move Files
  - `openhab2/items/*` -> `/etc/openhab2/items`
  - `openhab2/sitemaps/*` -> `/etc/openhab2/sitemaps`
  - `openhab2/rules/*` -> `/etc/openhab2/rules`
  - `openhab2/things/*` -> `/etc/openhab2/things`
  - `openhab2/services/*` -> `/etc/openhab2/services`
- Start `openhab2` service

## Docs

- [Openhab2](https://www.openhab.org/docs/)
- [MQTT2 Binding](https://www.openhab.org/addons/bindings/mqtt/)
- [Tasmota](https://github.com/arendst/Sonoff-Tasmota/wiki)
- [Sonoff](https://sonoff.itead.cc/en/products/residential/sonoff-t1-us)
