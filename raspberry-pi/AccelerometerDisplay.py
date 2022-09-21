from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import board
import time
import digitalio
import adafruit_mpu6050
import busio #import for all libraries
import adafruit_mpl3115a2

displayio.release_displays()

led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT #LED init

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP19)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) #Display init

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) #mpu init

sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)

initAlt = sensor.altitude

while True:
    x = round(mpu.acceleration[0], 3)
    y = round(mpu.acceleration[1], 3)
    z = round(mpu.acceleration[2], 3) #Pulls all the mpu acceleration values

    print(f"x: {x} m/s^2  y: {y} m/s^2 z: {z} m/s^2 \n Altitude: {sensor.altitude}") #Prints acceleration values with an f string
    splash = displayio.Group()

    # add title block to display group
    title = f"x: {x} m/s^2 \n y: {y} m/s^2 \n z: {z} m/s^2 \n ALTITUDE: {sensor.altitude}"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)    
    
    # send display group to screen
    display.show(splash)

    currentAlt = sensor.altitude
    altDifference = (currentAlt - initAlt)
    if z < 1 and z > -1 and altDifference < 3: #Checks if it is 90 degree angle
        led.value = True
    else:
        led.value = False
    time.sleep(0.01)