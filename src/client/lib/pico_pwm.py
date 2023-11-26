from machine import PWM
from machine import Pin

class pico_PWM():
    def __init__(self, pin):
        self.pin = PWM(Pin(pin, Pin.OUT))
        self.pin.freq(50)

