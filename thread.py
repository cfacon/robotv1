import random
import sys
from threading import Thread
import time

class Afficheur(Thread):


    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        i = 0
        while i < 20:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            i += 1



thread_1 = Afficheur("1")
thread_2 = Afficheur("2")

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
