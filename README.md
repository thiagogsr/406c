# House automation

## Getting start

- Flash a SD card with [Openhabian OS](https://www.openhab.org/docs/installation/openhabian.html)
- Fill `openhabian.conf` before first boot

## MQTT

Install que MQTT Server with `openhabian-config`

## Network

Set a fixed IP for the raspberry on your router.

## Broadlink

- Set the WiFi on your broadlink device with this [python package](https://github.com/mjg59/python-broadlink).
- Set a fixed IP for the broadlink device on your router.
- Clone [broadlink-mqtt](https://github.com/eschava/broadlink-mqtt.git) on home path

```
git clone https://github.com/eschava/broadlink-mqtt.git
```

Transfer the config file:

```
scp -r broadlink-mqtt/custom.conf openhabian@[raspberry-ip]:~/broadlink-mqtt
```

Then install its requirements

```
pip3 install -r requirements.txt
```

Transfer broadlink commands

```
scp -r broadlink/* openhabian@[raspberry-ip]:~/broadlink-mqtt/commands
```

Ensure broadlink is connected on same network.

Transfer the service file:

```
scp broadlink-mqtt/broadlink-mqtt.service openhabian@[raspberry-ip]:/etc/systemd/system/broadlink-mqtt.service
```

Then start it

```
sudo systemctl enable broadlink-mqtt
sudo systemctl start broadlink-mqtt
```

## Speed test

Follow the instructions to install the cli: [https://www.speedtest.net/pt/apps/cli](https://www.speedtest.net/pt/apps/cli)

## OpenHAB

Transfer openhab Files

```
scp openhab/items/* openhabian@[raspberry-ip]:/etc/openhab/items
scp openhab/sitemaps/* openhabian@[raspberry-ip]:/etc/openhab/sitemaps
scp openhab/rules/* openhabian@[raspberry-ip]:/etc/openhab/rules
scp openhab/things/* openhabian@[raspberry-ip]:/etc/openhab/things
scp openhab/services/* openhabian@[raspberry-ip]:/etc/openhab/services
```

## Docs

- [Openhab](https://www.openhab.org/docs/)
- [MQTT2 Binding](https://www.openhab.org/addons/bindings/mqtt/)
- [Tasmota](https://github.com/arendst/Sonoff-Tasmota/wiki)
- [Sonoff](https://sonoff.itead.cc/en/products/residential/sonoff-t1-us)
- [SpeedTest](https://community.openhab.org/t/speedtest-cli-internet-up-downlink-measurement-integration/7611)
