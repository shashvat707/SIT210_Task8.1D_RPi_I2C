import time
import board
import busio
import adafruit_veml7700

# sudo pip3 install adafruit-circuitpython-veml7700
# VEML7700:
#       Pi 3V3(PIN-1) to sensor VIN
#       Pi GND(PIN-6) to sensor GND
#       Pi SCL(PIN-5) to sensor SCL
#       Pi SDA(PIN-3) to sensor SDA


i2c = busio.I2C(board.SCL, board.SDA)
veml7700 = adafruit_veml7700.VEML7700(i2c)
 
while True:
    amb_light = veml7700.light
    print("Ambient light:", amb_light)
    # "too bright", "bright", "medium", "dark" and "too dark" 
    if amb_light > 16000:
        print ("too bright")
    elif amb_light > 12000:
        print ("bright")
    elif amb_light > 8000:
        print ("medium")
    elif amb_light > 4000:
        print ("dark")
    else :
        print ("too dark")
    time.sleep(0.1)
