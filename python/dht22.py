import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
timeout = 60

sensor = Adafruit_DHT.DHT22
sensor_pin = 23

try:
  client = mqtt.Client()
  client.connect(broker, port, timeout)

  humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
  
  if humidity is not None and temperature is not None:
    client.publish("home/office/temperature", '{0:0.1f}'.format(temperature), qos=0, retain=True)
    client.publish("home/office/humidity", '{0:0.1f}'.format(humidity), qos=0, retain=True)
  else:
    client.disconnect()
    print("Failed to get reading. Try again!")
    sys.exit(1)
except:
  print("Failed to execute program")
  sys.exit(1)
