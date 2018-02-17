import os
import re
import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
timeout = 60

try:
  client = mqtt.Client()
  client.connect(broker, port, timeout)

  temperature = os.popen("vcgencmd measure_temp").readline()
  temperature = re.sub(r"[^0-9.]", "", temperature)
  client.publish("rpi/temperature", temperature, qos=0, retain=True)

except:
  print("Failed to execute program")
  sys.exit(1)
