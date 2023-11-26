#Name:      main.py
#Date:      18.11.2023
#Author:    Iljadin Manurung
import _thread



def system_threading():
    second_thread = _thread.start_new_thread(core1_thread, ())
    core0_thread()
    pass

def core0_thread():
    pass


def core1_thread():
    pass


if __name__ == "__main__":
    system_threading()
    print("running")
