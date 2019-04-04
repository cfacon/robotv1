import datetime
import bottle
#import globalConfig, action
import action
from bottle import route, run, request, response, redirect, template, static_file
import os.path, functools
try:
    import configparser as cp
except ImportError:
    import ConfigParser as cp


globalConfig = cp.ConfigParser()
globalConfig.read('./globalConfig.cfg')

#abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
#abs_views_path = os.path.join(abs_app_dir_path, 'views')
bottle.TEMPLATE_PATH.insert(0, '/home/pi/robotRelease/robotv1/views')

@bottle.route("/")
@bottle.view("joy.tpl")
def index() :
  print ("ok")
#  return {"title":"robot", "body" : ""}
  return {"title":"robot",
                "body" : "",
                "moteur1_enA" : globalConfig['gpio']['moteur1_enA']
        }



@bottle.route("/settings")
@bottle.view("settings.tpl")
def settings() :
  print ("ok")
  ip = bottle.request.forms.get('ip')

  return {"title":"robot settings", 
		"body" : ip,
                "moteur1_enA" : globalConfig['gpio']['moteur1_enA']
	}

@bottle.route("/settings", method='POST')
@bottle.view("settings.tpl")
def settings() :
  print ("ok")
  ip = bottle.request.forms.get('ip')

  globalConfig['gpio']['moteur1_enA'] = bottle.request.forms.get('moteur1_enA')

  #Ecrire le fichier de configuration
  with open('globalConfig.cfg','w') as settings:
      globalConfig.write(settings)

  return {"title":"robot settings",
                "body" : ip,
                "moteur1_enA" : globalConfig['gpio']['moteur1_enA']
        }


#  return {"title":"robot settings", "body" : ip}



@bottle.route('/assets/<filepath:path>')
def assets(filepath):
  return static_file(filepath, root='/home/pi/robotRelease/robotv1/assets/')


@route('/cmd/<cmd>')
def controls(cmd):

  if globalConfig.dir != cmd:
    globalConfig.dir = cmd
    print ("_____cmd:"+cmd)
    action.action(cmd)
  return ''


def start():
  bottle.run(host='0.0.0.0', port=globalConfig['server']['port'])
  action.init()
  #start()
  return ''

