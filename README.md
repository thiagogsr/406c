### Important

1. Add `openhab` to `gpio` group: `sudo adduser openhab gpio`

### Files

- `406c.items` -> `/etc/openhab2/items/406c.items`
- `406c.sitemap` -> `/etc/openhab2/sitemaps/406c.sitemap`
- `mqtt.cfg` -> `/etc/openhab2/services/mqtt.cfg`

### Cronjob

- `*/5 * * * * /usr/bin/python /path_to_dht22.py`
- `*/5 * * * * /usr/bin/python /path_to_rpi.py`

### KB

- https://docs.openhab.org/configuration/index.html
- http://www.instructables.com/id/Installing-MQTT-BrokerMosquitto-on-Raspberry-Pi/
- https://www.embarcados.com.br/raspberry-pi-3-na-iot-mqtt-e-python/
- https://docs.openhab.org/addons/bindings/mqtt1/readme.html
- https://www.hackster.io/adamgarbo/raspberry-pi-2-iot-thingspeak-dht22-sensor-b208f4
- https://medium.com/@kevalpatel2106/monitor-the-core-temperature-of-your-raspberry-pi-3ddfdf82989f