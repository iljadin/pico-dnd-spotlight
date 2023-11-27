#---------------------------------------#  
# Class:    Servo                          #
# Date:     19.11.2023                      #
# Author:   Iljaidn Manurung            #
#---------------------------------------#  
from machine import PWM
from machine import Pin
from utime import sleep_ms

class Servo:
    def __init__(self, pin):
        self.pin = PWM(Pin(pin, Pin.OUT))
        self.pin.freq(50)

        self.min_duty = 3000 #Absolut Max 2500
        self.max_duty = 6300 #Absolut Max 7300
        self.mid_duty = 5000

    def move(self,duty):
        self.pin.duty_u16(duty)
        


if __name__ == "__main__":
    s1 = Servo(Pin(0))
    s2 = Servo(Pin(1))
    while(True):
        s1.move(6300)
        s2.move(3000)
        sleep_ms(2000)
        s1.move(3000)
        s2.move(7300)
        sleep_ms(2000)


