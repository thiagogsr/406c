# House automation

- Flash a SD card with [Openhabian OS](https://www.openhab.org/docs/installation/openhabian.html)

- Edit `/etc/openhabian.conf` and reboot the system

- Install que MQTT Server with `openhabian-config`

- Transfer openhab2 Files


      scp openhab2/items/* openhabian@[openhabian-ip]:/etc/openhab2/items
      scp openhab2/sitemaps/* openhabian@[openhabian-ip]:/etc/openhab2/sitemaps
      scp openhab2/rules/* openhabian@[openhabian-ip]:/etc/openhab2/rules
      scp openhab2/things/* openhabian@[openhabian-ip]:/etc/openhab2/things
      scp openhab2/services/* openhabian@[openhabian-ip]:/etc/openhab2/services


- Clone [broadlink-mqtt](https://github.com/eschava/broadlink-mqtt.git) on home path


    git clone https://github.com/eschava/broadlink-mqtt.git


- Then install its requirements


    pip install -r requirements.txt


- Transfer broadlink commands


    scp -r broadlink/* openhabian@[openhabian-ip]:~/broadlink-mqtt/commands


Ensure broadlink is connected on same network. Use this [python package](https://github.com/mjg59/python-broadlink)
to write the WiFi SSID on device.

- Start `broadlink-mqtt` with `python mqtt.py`

## Docs

- [Openhab2](https://www.openhab.org/docs/)
- [MQTT2 Binding](https://www.openhab.org/addons/bindings/mqtt/)
- [Tasmota](https://github.com/arendst/Sonoff-Tasmota/wiki)
- [Sonoff](https://sonoff.itead.cc/en/products/residential/sonoff-t1-us)
