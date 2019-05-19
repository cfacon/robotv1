#!/usr/bin/env python
# -*- coding: utf-8 -*-
#/dev/ttyUSB0

import serial
from time import sleep



FREQUENCE = 30
VITESSE = 100
ser = serial.Serial('/dev/ttyUSB0', 9600)

flag = 0
while(true)
    print(ser.readline())  #on affiche la réponse
    print "on attend 3s que l'arduino se prepare"    
#    sleep(4)   #on attend un peu, pour que l'Arduino soit prêt.
    
    
def init():
    print "on attend 3s que l'arduino se prepare"    
    #ser = serial.Serial('/dev/ttyUSB0', 9600)

    # AVANCE
def speed(speed):
    print("---change moteur vitesse")
    ser.write(speed)
    print(ser.readline())  #on affiche la réponse

def up():
    print("---moteur up")
    ser.write(str.encode('2'))
    print(ser.readline())  #on affiche la réponse
    
    
def down():
    print("---moteur down")
    ser.write(str.encode('3'))
    print(ser.readline())  #on affiche la réponse


def stop():
    print("moteur stop")
    ser.write(str.encode('1'))
    print(ser.readline())  #on affiche la réponse
    
def left():
    print("moteur left")
    ser.write(str.encode('6'))
    print(ser.readline())  #on affiche la réponse

def right():
    print("moteur right")
    ser.write(str.encode('7'))
    print(ser.readline())  #on affiche la réponse

