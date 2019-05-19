#!/usr/bin/env python
# -*- coding: latin-1 -*-


# server event side
from gevent import monkey; monkey.patch_all()
from gevent import sleep

from time import sleep
import time
import datetime
import bottle
from bottle import get, post
from bottle import route, run, request, response, redirect, template, static_file, GeventServer
import os.path, functools
try:
    import configparser as cp
except ImportError:
    import ConfigParser as cp

import threading

# serial pour communiquer avec arduino
import serial

# mqtt
import paho.mqtt.publish as publish

######################
#debut test sonar
#import RPi.GPIO as GPIO
import time


#fin test sonar
#####################


globalConfig = cp.ConfigParser()
globalConfig.read('/home/pi/robotRelease/robotv1/globalConfig.cfg')

#abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
#abs_views_path = os.path.join(abs_app_dir_path, 'views')
bottle.TEMPLATE_PATH.insert(0, '/home/pi/robotRelease/robotv1/views')

@bottle.route("/")
@bottle.view("joy.tpl")
def index() :
  print ("ok")
  return {"title":"robot",
                "body" : "",
                "vitesse" : globalConfig['divers']['vitesse'],
                "moteur1_enA" : globalConfig['gpio']['moteur1_enA'],
                "moteur1_en1" : globalConfig['gpio']['moteur1_en1'],
                "moteur1_en2" : globalConfig['gpio']['moteur1_en2'],
                "moteur2_enB" : globalConfig['gpio']['moteur2_enB'],
                "moteur2_en1" : globalConfig['gpio']['moteur2_en1'],
                "moteur2_en2" : globalConfig['gpio']['moteur2_en2']
        }



@bottle.route("/settings")
@bottle.view("settings.tpl")
def settings() :
  print ("ok")
  ip = bottle.request.forms.get('ip')

  return {"title":"robot settings", 
		"body" : ip,
                "vitesse" : globalConfig['divers']['vitesse'],
                "moteur1_enA" : globalConfig['gpio']['moteur1_enA'],
                "moteur1_en1" : globalConfig['gpio']['moteur1_en1'],
                "moteur1_en2" : globalConfig['gpio']['moteur1_en2'],
                "moteur2_enB" : globalConfig['gpio']['moteur2_enB'],
                "moteur2_en1" : globalConfig['gpio']['moteur2_en1'],
                "moteur2_en2" : globalConfig['gpio']['moteur2_en2']
	}

@bottle.route("/settings", method='POST')
@bottle.view("settings.tpl")
def settings() :
  print ("ok")
  ip = bottle.request.forms.get('ip')
  globalConfig['divers']['vitesse'] = bottle.request.forms.get('vitesse')

  # envois a l'arduino la nouvelle vitesse
  publish.single("robot/commande", globalConfig['divers']['vitesse'], hostname="localhost")

  globalConfig['gpio']['moteur1_enA'] = bottle.request.forms.get('moteur1_enA')
  globalConfig['gpio']['moteur1_en1'] = bottle.request.forms.get('moteur1_en1')
  globalConfig['gpio']['moteur1_en2'] = bottle.request.forms.get('moteur1_en2')
  globalConfig['gpio']['moteur2_enB'] = bottle.request.forms.get('moteur2_enB')
  globalConfig['gpio']['moteur2_en1'] = bottle.request.forms.get('moteur2_en1')
  globalConfig['gpio']['moteur2_en2'] = bottle.request.forms.get('moteur2_en2')


  #Ecrire le fichier de configuration
  with open('globalConfig.cfg','w') as settings:
      globalConfig.write(settings)

  return {"title":"robot settings",
                "body" : ip,
                "vitesse" : globalConfig['divers']['vitesse'],
                "moteur1_enA" : globalConfig['gpio']['moteur1_enA'],
                "moteur1_en1" : globalConfig['gpio']['moteur1_en1'],
                "moteur1_en2" : globalConfig['gpio']['moteur1_en2'],
                "moteur2_enB" : globalConfig['gpio']['moteur2_enB'],
                "moteur2_en1" : globalConfig['gpio']['moteur2_en1'],
                "moteur2_en2" : globalConfig['gpio']['moteur2_en2']
        }


@bottle.route('/assets/<filepath:path>')
def assets(filepath):
  return static_file(filepath, root='/home/pi/robotRelease/robotv1/assets/')


@route('/cmd/<cmd>')
def controls(cmd):

  if globalConfig['general']['dir'] != cmd:
    globalConfig['general']['dir'] = cmd
#    print ("cmd=:"+cmd)
    
    # ancien mode avec GPIO
    #threading.Thread(target=action.action(cmd)).start()

    #nouveau avec arduino et serial port via client_mqtt
    publish.single("robot/commande", cmd, hostname="localhost")
    
    
  return ''

@route('/sonar/', method='GET')
@bottle.view("sonar.tpl")
def sonar():

    print ("=========SONAR=============:")
    
    response.content_type  = 'text/event-stream'
    response.cache_control = 'no-cache'
    yield 'retry: 100\n\n'
    
    while True:
        global position,  arrivee
        if position < arrivee:  # si nous ne sommes pas pas arrivés, 
                                # nous avançons un peu
             pwm.ChangeDutyCycle(float(position))  
             position = position + 0.2
             time.sleep (0.05)
             distance = radar()
#             print "La distance est de : ",distance," cm"

             # Set client-side auto-reconnect timeout, ms.
             #yield 'event : sonar \n\n'                
             #yield 'data : '+ str(distance)+'\n\n'  
             #yield 'data: {"distance": "' + str(distance)+ '"}\n\n';
            
             yield 'event: distance\n data: '+ str(distance)+' \n\n';
                
        else:
             position = depart  # si nous sommes arrivés, 
                                # retour à la position de départ
    pwm.stop
    
    
@route('/sonar2/', method='GET')
@bottle.view("sonar.tpl")
def sonar():
    return {"title":"Horloge"}  

def start():
  bottle.run(host='0.0.0.0', port=globalConfig['server']['port'])
#  action.init()

    
    
  #start()
  return ''

