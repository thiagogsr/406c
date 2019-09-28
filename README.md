# House automation

## Getting start

- Flash a SD card with [Openhabian OS](https://www.openhab.org/docs/installation/openhabian.html)
- Fill `openhabian.conf` before first boot

## MQTT

Install que MQTT Server with `openhabian-config`

## Networking

Set a fixed IP

```
sudo vim /etc/dhcpcd.conf
```

Replace the `# Example static IP configuration:` section with:

```
interface eth0
static ip_address=192.168.0.113/24
#static ip6_address=fd51:42f8:caae:d92e::ff/64
static routers=192.168.0.1
static domain_name_servers=192.168.0.1
```

Export the openhabian IP on your machine to transfer the files

```
export OPENHAB_IP=192.168.0.113
```

## Broadlink

- Set the WiFi on your broadlink with this [python package](https://github.com/mjg59/python-broadlink).
- Clone [broadlink-mqtt](https://github.com/eschava/broadlink-mqtt.git) on home path

```
git clone https://github.com/eschava/broadlink-mqtt.git
```

Edit the `custom.conf` with:

```
device_type = 'rm'
device_host = '192.168.0.105'
device_mac = '78:0f:77:b9:28:6b'
```

Then install its requirements

```
pip install -r requirements.txt
```

Transfer broadlink commands

```
scp -r broadlink/* openhabian@$OPENHAB_IP:~/broadlink-mqtt/commands
```

Ensure broadlink is connected on same network. Use this

Start `broadlink-mqtt` with `python mqtt.py &`

## Speed test

Install easy_install if not yet available

```
sudo python /usr/lib/python2.7/dist-packages/easy_install.py speedtest-cli
```

## OpenHAB2

Transfer openhab2 Files

```
scp openhab2/items/* openhabian@$OPENHAB_IP:/etc/openhab2/items
scp openhab2/sitemaps/* openhabian@$OPENHAB_IP:/etc/openhab2/sitemaps
scp openhab2/rules/* openhabian@$OPENHAB_IP:/etc/openhab2/rules
scp openhab2/things/* openhabian@$OPENHAB_IP:/etc/openhab2/things
scp openhab2/services/* openhabian@$OPENHAB_IP:/etc/openhab2/services
```

## Docs

- [Openhab2](https://www.openhab.org/docs/)
- [MQTT2 Binding](https://www.openhab.org/addons/bindings/mqtt/)
- [Tasmota](https://github.com/arendst/Sonoff-Tasmota/wiki)
- [Sonoff](https://sonoff.itead.cc/en/products/residential/sonoff-t1-us)
- [SpeedTest](https://community.openhab.org/t/speedtest-cli-internet-up-downlink-measurement-integration/7611)
