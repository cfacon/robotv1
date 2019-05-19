#!/usr/bin/env python
# -*- coding: latin-1 -*-

'''
Contrôle d'un servomoteur avec un Raspberry Pi
Le servo tourne lentement dans une direction, et
retourne rapidement à sa position de départ.
Pour plus de détails:
http://electroniqueamateur.blogspot.com/2015/11/controler-un-servomoteur-en-python-avec.html
'''

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


   

while True:
        global position,  arrivee
        if position < arrivee:  # si nous ne sommes pas pas arrivés, 
                                # nous avançons un peu
             pwm.ChangeDutyCycle(float(position))  
             position = position + 0.2
             time.sleep (0.05)
             #distance = sonar()
#             print "La distance est de : ",distance," cm"

             # Set client-side auto-reconnect timeout, ms.
             #yield 'disctance: '+distance+' cm\n\n'                
                
        else:
             position = depart  # si nous sommes arrivés, 
                                # retour à la position de départ
pwm.stop
GPIO.cleanup()
