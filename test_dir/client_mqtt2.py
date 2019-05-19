import time
import paho.mqtt.client as mqtt

# Will be called upon reception of CONNACK response from the server.
def on_connect(client, data, flags, rc):
    client.subscribe("robot/commande", 1)

def on_message(client, data, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Set the username to 'token:CHANNEL_TOKEN' before calling connect
client.username_pw_set("token:YOUR_CHANNEL_TOKEN")
# Alternatively, set the username to your SECRET KEY
#client.username_pw_set('YOUR_SECRET_KEY')
client.connect("localhost", 1883, 60)

client.loop_start()

while 1:
   time.sleep(1)
