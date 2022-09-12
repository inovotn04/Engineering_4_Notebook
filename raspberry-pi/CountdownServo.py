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

pwm_servo = pwmio.PWMOut(board.GP2, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0

while True:
    if not button.value:
        print("Countdown time")
        abortcheck = 0
        x = 10
        ang = 0
        for x in range (10, -1, -1):
            if x == 3:
                servo.angle = ang
            print(x)
            time.sleep(0.5)
            if not button.value:
                abortcheck = 1
                break
            led_red.value = True
            time.sleep(0.5)
            led_red.value = False
            if not button.value:
                abortcheck = 1
                break
        if abortcheck == 1:
            print("ABORT")
            time.sleep(2)
        if abortcheck == 0:
            servo1.angle = 180
            print("Liftoff")
            led_green.value = True
            time.sleep(10)
            servo1.angle = 180
