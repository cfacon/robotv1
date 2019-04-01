from time import sleep
import RPi.GPIO as GPIO
import globalConfig

MOTOR1_EN = globalConfig.moteur1_enA
MOTOR1_A = globalConfig.moteur1_en1
MOTOR1_B = globalConfig.moteur1_en2

MOTOR2_EN = globalConfig.moteur2_enB
MOTOR2_A = globalConfig.moteur2_en1
MOTOR2_B = globalConfig.moteur2_en2

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
    motor1GPIO = GPIO.PWM(MOTOR1_EN, 50)
    motor2GPIO = GPIO.PWM(MOTOR2_EN, 50)

    motor1GPIO.start(globalConfig.moteur_vitesse)
    motor2GPIO.start(globalConfig.moteur_vitesse)

    # AVANCE
def up():
    # a 20% de sa vitesse
    print("moteur up")
    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.LOW)

    GPIO.output(MOTOR2_EN, GPIO.HIGH)
    GPIO.output(MOTOR2_A, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.LOW)

def down():
    # a 20% de sa vitesse
    print("moteur down")
    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.LOW)
 
    GPIO.output(MOTOR2_EN, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.HIGH)
    GPIO.output(MOTOR2_A, GPIO.LOW)

    # Stoppe et freine les moteurs pendant une seconde
def stop():
    print("moteur stop")
    GPIO.output(MOTOR1_EN, GPIO.LOW)
    GPIO.output(MOTOR2_EN, GPIO.LOW)
    #sleep(1)

    # TOURNE A GAUCHE
def left():
    print("moteur left")
    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.HIGH)

    GPIO.output(MOTOR2_EN, GPIO.HIGH)
    GPIO.output(MOTOR2_A, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.LOW)

def right():
    print("moteur right")
    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.HIGH)

    GPIO.output(MOTOR2_EN, GPIO.HIGH)
    GPIO.output(MOTOR2_A, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.LOW)

#try
#except:
#  GPIO.cleanup()
#  raise

