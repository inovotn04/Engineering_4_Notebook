
import board
import digitalio
import time #import libraries

led = digitalio.DigitalInOut(board.LED) #Define LED on the board
led.direction = digitalio.Direction.OUTPUT #Set to output

while True:
    led.value = True #Led on
    time.sleep(1) #wait
    led.value = False #Led off
    time.sleep(1)
