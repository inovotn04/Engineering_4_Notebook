import board
import time
import digitalio
import pwmio
from adafruit_motor import servo

led_red = digitalio.DigitalInOut(board.GP13) #Defines led_red to be GP13 pin
led_red.direction = digitalio.Direction.OUTPUT #Sets red led to output

led_green = digitalio.DigitalInOut(board.GP18) #Defines led_green to be GP18 pin
led_green.direction = digitalio.Direction.OUTPUT #Sets green led to output

led_green.value = False #Makes sure green led starts off (just in case)


button = digitalio.DigitalInOut(board.GP16) #Defines button to be GP16 pin
button.direction = digitalio.Direction.INPUT #Sets button to input
button.pull = digitalio.Pull.UP #Sets button to pull down (only used with ground wiring)


pwm_servo = pwmio.PWMOut(board.GP2, duty_cycle=2 ** 15, frequency=50) #Servo settings
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500) #Defines servo variable
servo1.angle = 0 #Sets initial servo angle

while True:
    if not button.value: #Checks if button is pressed (changed for other button wiring)
        print("Countdown time")
        abortcheck = 0 #Sets check if button has been pressed a second time to 0
        x = 10
        for x in range (10, -1, -1):
            print(x)
            time.sleep(0.5)
            if not button.value: #Checks if button has been pressed a second time
                abortcheck = 1 #Signals button has been pressed a second time
                break
            led_red.value = True #Red led on
            time.sleep(0.5)
            led_red.value = False #Red led off
            if not button.value:
                abortcheck = 1
                break
        if abortcheck == 1: #If button has been pressed a second time, print("ABORT")
            print("ABORT")
        if abortcheck == 0: #If button hasn't, print("Liftoff")

            servo1.angle = 180 #And turn servo
            print("Liftoff")
            led_green.value = True #And turn on green led
            time.sleep(10)
