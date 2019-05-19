#!/usr/bin/env python
# -*- coding: latin-1 -*-



import RPi.GPIO as GPIO
import time

servo_pin = 18  # gpio18

depart = 8      # rapport cyclique pour que le servo 
                # soit au début de son mouvement
                # à ajuster pour votre servo!

arrivee = 20    # rapport cyclique pour que le servo 
                # soit à la fin de son mouvement
                # à ajuster pour votre servo!
     
GPIO.setmode(GPIO.BCM)  # notation board plutôt que BCM

GPIO.setup(servo_pin, GPIO.OUT)  # pin configurée en sortie

pwm = GPIO.PWM(servo_pin, 100)  # pwm à une fréquence de 50 Hz

position = depart   # on commence à la position de départ

pwm.start(depart)  # on commence le signal pwm

def sonar():
   Trig = 23          # Entree Trig du HC-SR04 branchee au GPIO 23
   Echo = 24         # Sortie Echo du HC-SR04 branchee au GPIO 24

   GPIO.setup(Trig,GPIO.OUT)
   GPIO.setup(Echo,GPIO.IN)    
   
   GPIO.output(Trig, True)
   time.sleep(0.00001)
   GPIO.output(Trig, False)
   debutImpulsion = 0
   finImpulsion = 0
    
   while GPIO.input(Echo)==0:  ## Emission de l'ultrason
     debutImpulsion = time.time()

   while GPIO.input(Echo)==1:   ## Retour de l'Echo
     finImpulsion = time.time()

   distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s

   #print "La distance est de : ",distance," cm"
   return distance

   
from bottle import Bottle

server1 = Bottle()
@server1.route('/')
def root():
    return 'Hello from sub app 1'

def init(response):
    #GPIO.cleanup()
    print '-------init sonar2--------'
    
#    response.content_type  = 'text/event-stream'
#    response.cache_control = 'no-cache'
#    yield 'init' 
    
    while True:
        global position,  arrivee
        if position < arrivee:  # si nous ne sommes pas pas arrivés, 
                                # nous avançons un peu
             pwm.ChangeDutyCycle(float(position))  
             position = position + 0.2
             time.sleep (0.05)
             distance = sonar()
             print "La distance est de : ",distance," cm"

             # Set client-side auto-reconnect timeout, ms.
             #yield 'disctance: '+distance+' cm\n\n'                
                
        else:
             position = depart  # si nous sommes arrivés, 
                                # retour à la position de départ
    pwm.stop
