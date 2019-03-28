from time import sleep
import RPi.GPIO as GPIO

MOTOR1_EN = 14
MOTOR1_A = 20
MOTOR1_B = 21

try:

    # Configure les pins
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(MOTOR1_EN, GPIO.OUT)
    GPIO.setup(MOTOR1_A, GPIO.OUT)
    GPIO.setup(MOTOR1_B, GPIO.OUT)

    # 0/100% pour la vitesse
    motor1GPIO = GPIO.PWM(MOTOR1_EN, 100)

    # AVANCE

    # a 50% de sa vitesse
    motor1GPIO.start(50)

    GPIO.output(MOTOR1_A, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.LOW)


    # Continu d'avancer pendant une seconde
    sleep(1)

    # Stoppe et freine les moteurs pendant une seconde
    GPIO.output(MOTOR1_EN, GPIO.LOW)
    sleep(1)

    # TOURNE A GAUCHE

    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.LOW)
    GPIO.output(MOTOR1_B, GPIO.HIGH)

    sleep(0.5)

    GPIO.output(MOTOR1_EN, GPIO.LOW)

    sleep(1)

    GPIO.output(MOTOR1_EN, GPIO.LOW)

except KeyboardInterrupt:
    pass
except:
    GPIO.cleanup()
    raise

GPIO.cleanup()
