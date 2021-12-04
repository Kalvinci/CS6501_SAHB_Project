from TCS34725 import TCS34725
from blinkytape import BlinkyTape

lux_requirements = {
    "working": 100,
    "meeting": 200,
    "reading": 300
}

bb = BlinkyTape('/dev/ttyACM0', 120)
sensor = TCS34725(0X29, debug=False)
sensor.TCS34725_init()

def turnOff():
    bb.displayColor(0, 0, 0)

def actuate(task):
    try:
        turnOff()
        
        sensor.Get_RGBData()
        sensor.GetRGB888()
        lux = sensor.Get_Lux()
        R = sensor.RGB888_R
        G = sensor.RGB888_G
        B = sensor.RGB888_B
        
        if lux >= lux_requirements[task]:
            bb.displayColor(50, 50, 50)
        else:
            bb.displayColor(255, 255, 255)
                
        return {
            "lux": lux,
            "R": R,
            "G": G,
            "B": B
        }
    except Exception as e:
        print("Error! \n", e)