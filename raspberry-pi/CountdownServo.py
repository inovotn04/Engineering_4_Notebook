import board
import time
import digitalio
import pwmio
from adafruit_motor import servo

led_red = digitalio.DigitalInOut(board.GP13)
led_red.direction = digitalio.Direction.OUTPUT
led_green = digitalio.DigitalInOut(board.GP18)
led_green.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

led_green.value = False

while True:
    if not button.value:
        print("Countdown time")
        Hehe = 0
        x = 10
        for x in range (10, -1, -1):
            print(x)
            time.sleep(0.5)
            if not button.value:
                Hehe = 1
                break
            led_red.value = True
            time.sleep(0.5)
            led_red.value = False
            if not button.value:
                Hehe = 1
                break
        if Hehe == 1:
            print("ABORT")
            time.sleep(2)
        if Hehe == 0:

            print("Liftoff")
            led_green.value = True
            time.sleep(10)
