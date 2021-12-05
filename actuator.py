from TCS34725 import TCS34725
from blinkytape import BlinkyTape
from threading import Thread
import time

task = None

stop_threads = False
thread = None

requirements = {
    "reading": { "lux": 300, "color": (0, 0, 155) },
    "meeting": { "lux": 200, "color": (155, 0, 0) },
    "working": { "lux": 100, "color": (0, 155, 0) }
}

bb = BlinkyTape('/dev/ttyACM0', 120)
sensor = TCS34725(0X29, debug=False)
sensor.TCS34725_init()

class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        self.get_lux()

    def get_lux(self):
        global stop_threads
        while True:
            if stop_threads:
                break
            sensor.Get_RGBData()
            luxval = sensor.Get_Lux()
            if task != None:
                R, G, B = requirements[task]["color"]
                if luxval >= requirements[task]["lux"]:
                    bb.displayColor(R, G, B)
                else:
                    bb.displayColor(R+100, G+100, B+100)
            time.sleep(2)

def turnOff():
    try:
        global stop_threads, thread
        stop_threads = True
        bb.displayColor(0, 0, 0)
        if thread:
            thread.join()
        return 0
    except Exception as e:
        print("Poweroff Error! \n", e)
        return 1

def actuate(t):
    try:
        global task, stop_threads
        task = t

        stop_threads = False
        thread = MyThread()
        thread.start()

        R, G, B = requirements[task]["color"]
        bb.displayColor(R, G, B)

        return 0
    except Exception as e:
        print("Actuate Error! \n", e)
        return 1