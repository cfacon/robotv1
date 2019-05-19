import RPi.GPIO as GPIO
import time

GPIO_NUMBER = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_NUMBER, GPIO.OUT)
GPIO.setwarnings(False)

ajoutAngle = 5
nbrTour = 1

def servo():
    pwm=GPIO.PWM(GPIO_NUMBER,100)
    pwm.start(50)

    angle1 = 0
    duty1 = float(angle1)/10 + ajoutAngle
    duty1 = 1

    angle2=180
    duty2= float(angle2)/10 + ajoutAngle

    i = 0

    while i <= nbrTour:
         pwm.ChangeDutyCycle(duty1)
         time.sleep(0.8)
         pwm.ChangeDutyCycle(duty2)
         time.sleep(0.8)
         i = i+1
    GPIO.cleanup()

servo()