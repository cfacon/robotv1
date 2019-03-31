import datetime
import bottle
import globalConfig, action
from bottle import route, run, request, response, redirect, template, static_file

@bottle.route("/")
@bottle.view("joy.tpl")
def index() :
  print ("ok")
  heure = datetime.datetime.now().strftime("<p>Nous sommes le %d/%m/%Y, il est %H:%M:%S</p>")
  return {"title":"Horloge", "body" : heure}
#  return ''

@bottle.route('/assets/<filepath:path>')
def assets(filepath):
  return static_file(filepath, root='assets/')


@route('/cmd/<cmd>')
def controls(cmd):

  if globalConfig.dir != cmd:
    globalConfig.dir = cmd
    print ("_____cmd:"+cmd)
    action.action(cmd)
  return ''


@route('/controls/<stick1x>/<stick1y>/<stick2x>/<stick2y>')
def controls(stick1x, stick1y, stick2x, stick2y):
  print (stick1x + stick1y + stick2x + stick2y)
  globalConfig.leftJoystickX = int(stick1x)
  globalConfig.leftJoystickY = int(stick1y)
  globalConfig.rightJoystickX = int(stick2x)
  globalConfig.rightJoystickY = int(stick2y)
  globalConfig.lastHTTPrequest = time.time()
  return 'stick1x = ' + stick1x + " stick1y = " + stick1y + " stick2x = " + stick2x + " stick2y = " + stick2y

#bottle.run(bottle.app(), host='0.0.0.0', port=8080, debug= False, reloader=True)
def start():
  bottle.run(host='0.0.0.0', port=8080)
  return ''

action.init()
start()
