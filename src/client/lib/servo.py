#---------------------------------------#  
# Class:    Servo                          #
# Date:     19.11.2023                      #
# Author:   Iljaidn Manurung            #
#---------------------------------------#  
from machine import PWM
from machine import Pin

class Servo:
    def __init__(self, pin):
        self.pin = PWM(Pin(pin, Pin.OUT))
        self.pin.freq(50)
        self.min_duty = 3000 #Absolut Max 2500
        self.max_duty = 7000 #Absolut Max 7300
