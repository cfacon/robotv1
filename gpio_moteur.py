from time import sleep
import RPi.GPIO as GPIO

#test
MOTOR1_EN = 16
MOTOR1_A = 20
MOTOR1_B = 21

MOTOR2_EN = 13
MOTOR2_A = 26
MOTOR2_B = 19

#Motor1A = 35
#Motor1B = 37
#Motor1E = 33

#Motor2A = 40
#Motor2B = 38
#Motor2E = 36


FREQUENCE = 30
VITESSE = 100

def init():
    #test nettoyage
    GPIO.cleanup()

    # Configure les pins
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(MOTOR1_EN, GPIO.OUT)
    GPIO.setup(MOTOR1_A, GPIO.OUT)
    GPIO.setup(MOTOR1_B, GPIO.OUT)

    GPIO.setup(MOTOR2_EN, GPIO.OUT)
    GPIO.setup(MOTOR2_A, GPIO.OUT)
    GPIO.setup(MOTOR2_B, GPIO.OUT)

    # 0/100% pour la vitesse
    motor1GPIO = GPIO.PWM(MOTOR1_EN, FREQUENCE)
    motor2GPIO = GPIO.PWM(MOTOR2_EN, FREQUENCE)

    motor1GPIO.start(VITESSE)
    motor2GPIO.start(VITESSE)

    # AVANCE
def up():
    print("---moteur up")

    GPIO.cleanup()

    # Configure les pins
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(MOTOR1_EN, GPIO.OUT)
    GPIO.setup(MOTOR1_A, GPIO.OUT)
    GPIO.setup(MOTOR1_B, GPIO.OUT)

    GPIO.setup(MOTOR2_EN, GPIO.OUT)
    GPIO.setup(MOTOR2_A, GPIO.OUT)
    GPIO.setup(MOTOR2_B, GPIO.OUT)

    # 0/100% pour la vitesse
    motor1GPIO = GPIO.PWM(MOTOR1_EN, FREQUENCE)
    motor2GPIO = GPIO.PWM(MOTOR2_EN, FREQUENCE)

    # AVANCE

    # a 50% de sa vitesse
    motor1GPIO.start(VITESSE)
    motor2GPIO.start(VITESSE)

    GPIO.output(MOTOR1_A, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.LOW)

    GPIO.output(MOTOR2_A, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.LOW)
	 # Continu d'avancer pendant une seconde
    sleep(2)

    # Stoppe et freine les moteurs pendant une seconde
    GPIO.output(MOTOR1_EN, GPIO.LOW)
    GPIO.output(MOTOR2_EN, GPIO.LOW)
    sleep(1)





def down():
    print("---moteur down")
    init()

    GPIO.output(MOTOR1_B, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.LOW)

    GPIO.output(MOTOR2_B, GPIO.HIGH)
    GPIO.output(MOTOR2_A, GPIO.LOW)
    sleep(2)


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
    GPIO.output(MOTOR1_B, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.LOW)

    GPIO.output(MOTOR2_A, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.LOW)

def right():
    print("moteur right")
    init()

    GPIO.output(MOTOR1_A, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.LOW)

    GPIO.output(MOTOR2_B, GPIO.HIGH)
    GPIO.output(MOTOR2_A, GPIO.LOW)

#try
#except:
#  GPIO.cleanup()
#  raise
