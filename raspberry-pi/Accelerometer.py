import board
import time
import digitalio

led_blue = digitalio.DigitalInOut(board.GP13)
led_blue.direction = digitalio.Direction.OUTPUT

led_blue.value = False