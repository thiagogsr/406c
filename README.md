# House automation

- Flash a SD card with [Openhabian OS](https://www.openhab.org/docs/installation/openhabian.html)
- Edit `/etc/openhabian.conf` and reboot the system
- Install que MQTT Server with `openhabian-config`
- Move Files
  - `scp openhab2/items/* openhabian@openhab:/etc/openhab2/items`
  - `scp openhab2/sitemaps/* openhabian@openhab:/etc/openhab2/sitemaps`
  - `scp openhab2/rules/* openhabian@openhab:/etc/openhab2/rules`
  - `scp openhab2/things/* openhabian@openhab:/etc/openhab2/things`
  - `scp openhab2/services/* openhabian@openhab:/etc/openhab2/services`
- Reboot system

## Docs

- [Openhab2](https://www.openhab.org/docs/)
- [MQTT2 Binding](https://www.openhab.org/addons/bindings/mqtt/)
- [Tasmota](https://github.com/arendst/Sonoff-Tasmota/wiki)
- [Sonoff](https://sonoff.itead.cc/en/products/residential/sonoff-t1-us)
