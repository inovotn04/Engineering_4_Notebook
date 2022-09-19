import board
import time
import digitalio
import adafruit_mpu6050
import busio

led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT #LED init

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 

mpu = adafruit_mpu6050.MPU6050(i2c) #mpu init

while True:
    x = mpu.acceleration[0]
    y = mpu.acceleration[1]
    z = mpu.acceleration[2] #Pulls all the mpu acceleration values

    print(f"x: {x} m/s^2  y: {y} m/s^2 z: {z} m/s^2") #Prints acceleration values with an f string

    if z < 1 and z > -1: #Checks if it is 90 degree angle
        led.value = True
    else:
        led.value = False
    time.sleep(0.1)