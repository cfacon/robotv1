import moteur

def init():
  moteur.init()
  return

def action(cmd):
  if cmd == "left":
    print ("action left")
    moteur.left()
  elif cmd == "right":
    moteur.right()
  elif cmd == "up":
    moteur.up()
  elif cmd == "down":
    moteur.down()
  else:
    moteur.stop()

  return
