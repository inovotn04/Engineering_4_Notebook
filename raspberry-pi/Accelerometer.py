import board
import time
import adafruit_mpu6050
import busio  #import libraries

sda_pin = board.GP14
scl_pin = board.GP15 #defines pins
i2c = busio.I2C(scl_pin, sda_pin) #inits i2c device

mpu = adafruit_mpu6050.MPU6050(i2c) #inits mpu accelerometer

while True:
    x = mpu.acceleration[0]
    y = mpu.acceleration[1]
    z = mpu.acceleration[2] #Pulls all the mpu acceleration values

    print(f"x: {x} m/s^2  y: {y} m/s^2 z: {z} m/s^2") #Prints acceleration values with an f string
    time.sleep(0.2)