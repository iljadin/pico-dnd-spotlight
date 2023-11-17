from machine import Pin
from utime import sleep
import _thread

class LED:
    pin = Pin("LED", Pin.OUT)
    @classmethod
    def set_LED(cls):
        cls.pin.on()
    
    @classmethod
    def reset_LED(cls):
        cls.pin.off()
    
    @classmethod
    def get_LED(cls):
        return cls.pin.value()
    
    @classmethod
    def toggle_LED(cls):
        cls.pin.toggle()





def core0_thread():
    global lock
    global led
    while(True):
        lock.acquire()
        ()
        print("core0 aquired")
        for _ in range(5):
            led.toggle_LED()
            sleep(0.5)
            led.toggle_LED()
            sleep(0.5)
        lock.release()


def core1_thread():
    global lock
    global led
    while(True):
        lock.acquire()
        print("core1 aquired")
        for _ in range(5):
            led.toggle_LED()
            sleep(0.2)
            led.toggle_LED()
            sleep(0.2)
        lock.release()





led = LED()

lock = _thread.allocate_lock()

second_thread = _thread.start_new_thread(core1_thread, ())
core0_thread()