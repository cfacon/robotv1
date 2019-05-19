from time import sleep
import RPi.GPIO as GPIO
try:
    import configparser as cp
except ImportError:
    import ConfigParser as cp


globalConfig = cp.ConfigParser()
globalConfig.read('/home/pi/robotRelease/robotv1/globalConfig.cfg')



MOTOR1_EN = int(globalConfig['gpio']['moteur1_enA'])
MOTOR1_A = int(globalConfig['gpio']['moteur1_en1'])
MOTOR1_B = int(globalConfig['gpio']['moteur1_en2'])

MOTOR2_EN = int(globalConfig['gpio']['moteur2_enB'])
MOTOR2_A = int(globalConfig['gpio']['moteur2_en1'])
MOTOR2_B = int(globalConfig['gpio']['moteur2_en2'])
VITESSE = int(globalConfig['divers']['vitesse'])

#test

def init():
    #test nettoyage
    GPIO.cleanup()
    GPIO.setwarnings(False)

    # Configure les pins
    GPIO.setmode(GPIO.BOARD)
    #GPIO.setmode(GPIO.BCM)

    globalConfig = cp.ConfigParser()
    globalConfig.read('/home/pi/robotRelease/robotv1/globalConfig.cfg')
    MOTOR1_EN = int(globalConfig['gpio']['moteur1_enA'])
    MOTOR1_A = int(globalConfig['gpio']['moteur1_en1'])
    MOTOR1_B = int(globalConfig['gpio']['moteur1_en2'])

    MOTOR2_EN = int(globalConfig['gpio']['moteur2_enB'])
    MOTOR2_A = int(globalConfig['gpio']['moteur2_en1'])
    MOTOR2_B = int(globalConfig['gpio']['moteur2_en2'])
    VITESSE = int(globalConfig['divers']['vitesse'])

    print("init")
    print(MOTOR1_EN)
    print(MOTOR1_A)
    print(MOTOR1_B)

    print(MOTOR2_EN)
    print(MOTOR2_A)
    print(MOTOR2_B)

    GPIO.setup(MOTOR1_EN, GPIO.OUT)
    GPIO.setup(MOTOR1_A, GPIO.OUT)
    GPIO.setup(MOTOR1_B, GPIO.OUT)

    GPIO.setup(MOTOR2_EN, GPIO.OUT)
    GPIO.setup(MOTOR2_A, GPIO.OUT)
    GPIO.setup(MOTOR2_B, GPIO.OUT)

    # frequence
    motor1GPIO = GPIO.PWM(MOTOR1_EN, 30)
    motor2GPIO = GPIO.PWM(MOTOR2_EN, 30)

    # 0/100% pour la vitesse
    print("vitesse= {}".format(VITESSE))
    motor1GPIO.start(VITESSE)
    motor2GPIO.start(VITESSE)

    # AVANCE
def up():
    print("---moteur up")
    init()

#    GPIO.output(MOTOR2_EN, GPIO.HIGH)
    GPIO.output(MOTOR2_A, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.LOW)

#    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.LOW)
    sleep(1) 

def down():
    # a 20% de sa vitesse
    print("moteur down")
    init()
#    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.LOW)

#    GPIO.output(MOTOR2_EN, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.HIGH)
    GPIO.output(MOTOR2_A, GPIO.LOW)

    # Stoppe et freine les moteurs pendant une seconde
def stop():
    init()
    print("moteur stop")
    GPIO.output(MOTOR1_EN, GPIO.LOW)
    GPIO.output(MOTOR2_EN, GPIO.LOW)
    #sleep(1)

    # TOURNE A GAUCHE
def left():
    print("moteur left")
    init()
 #   GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.LOW)
    GPIO.output(MOTOR1_B, GPIO.HIGH)

 #   GPIO.output(MOTOR2_EN, GPIO.HIGH)
    GPIO.output(MOTOR2_A, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.LOW)

def right():
    print("moteur right")
    init()
 #   GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.LOW)

 #   GPIO.output(MOTOR2_EN, GPIO.HIGH)
    GPIO.output(MOTOR2_A, GPIO.LOW)
    GPIO.output(MOTOR2_B, GPIO.HIGH)

#try
#except:
#  GPIO.cleanup()
#  raise

