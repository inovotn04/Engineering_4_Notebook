import board
import time
import digitalio #importing libraries

led_red = digitalio.DigitalInOut(board.GP13) #Defines led_red to be GP13 pin
led_red.direction = digitalio.Direction.OUTPUT #Sets red led to output

led_green = digitalio.DigitalInOut(board.GP18) #Defines led_green to be GP18 pin
led_green.direction = digitalio.Direction.OUTPUT #Sets green led to output

led_green.value = False #Makes sure green led starts off (just in case)

print("Countdown time")
x = 10 #Sets x variable to 10 to work the for loop
for x in range (10, -1, -1): #for loop, counts down from 10, until it reaches -1
 print(x)
 time.sleep(0.5) #Split the 1 second in order to blink the led on and off in one loop
 led_red.value = True #Red led on
 time.sleep(0.5) 
 led_red.value = False #Red led off
print("Liftoff")
led_green.value = True #Green led on
time.sleep(10) #Delays the pico turning off so you can see the green led
