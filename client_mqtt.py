#!/usr/bin/env python
# -*- coding: utf-8 -*-
#/dev/ttyUSB0

import serial
from time import sleep

import paho.mqtt.client as mqtt #import the client1
import time

# trouve le port
import sys
import glob
import serial



# trouve le port usb
def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
#        ports = glob.glob('/dev/tty[A-Za-z]*')
        ports = glob.glob('/dev/ttyUSB*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = ""
    result = []

    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
#            result.append(port)
            result = port
        except (OSError, serial.SerialException):
            pass
    return result

def on_connect(client, data, flags, rc):
    client.subscribe("robot/commande", 1)
   
    
def action(cmd):
  print ("cmd=",cmd)
    
  if cmd == "4":
    ser.write(str.encode('4'))
  elif cmd == "1":
    ser.write(str.encode('1'))
  elif cmd == "5":
    ser.write(str.encode('5'))
  elif cmd == "2":
    print ("on a 2")
    ser.write(str.encode('2'))
  elif cmd == "3":
    ser.write(str.encode('3'))
  else:
    ser.write(str.encode(cmd))

#def on_message(client, q, message):
#    msg = message.payload.decode("utf-8")
#    action(msg)

def on_message(client, data, msg):
    print(msg.topic + " " + str(msg.payload))
    action(msg.payload.decode("utf-8"))


port = serial_ports()
ser = serial.Serial(port, 9600)
#ser = serial.Serial('/dev/ttyUSB0', 9600)
print ("wait 4s")
sleep(4)
print ("go")

# on commence par envoyer un stop
ser.write(str.encode('1'))
time.sleep(1)               # on attend pendant 1 seconde


########################################
#broker_address="localhost"
#print("creating new instance")
#client = mqtt.Client() #create new instance
#client.on_message=on_message #attach function to callback

#print("connecting to broker")
#client.connect(broker_address) #connect to broker
#client.loop_start() #start the loop

#topic = "robot/commande"
#print("Subscribing to topic",topic)
#client.subscribe(topic)

#client.loop_forever()
#quit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_start()

while 1:
   time.sleep(1)

