import paho.mqtt.client as mqtt
import sys

Broker = "localhost"
PortaBroker = 1883
KeepAliveBroker = 60
TopicoSubscribe = "PAHOMQTTRaspPi3"

def on_connect(client, userdata, flags, rc):
  print("[STATUS] Conectado ao Broker. Resultado de conexao: " + str(rc))
  client.subscribe(TopicoSubscribe)

def on_message(client, userdata, msg):
	MensagemRecebida = str(msg.payload)
	print("[MSG RECEBIDA] Topico: " + msg.topic + " / Mensagem: " + MensagemRecebida)

try:
  print("[STATUS] Inicializando MQTT...")
  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message
  client.connect(Broker, PortaBroker, KeepAliveBroker)
  client.loop_forever()
except KeyboardInterrupt:
  print "\nCtrl+C pressionado, encerrando aplicacao e saindo..."
  sys.exit(0)
