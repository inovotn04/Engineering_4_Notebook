import board
import time
import digitalio


print("Countdown time")
x = 10
for x in range (10, -1, -1):
 print(x)
 time.sleep(1)
print("Liftoff")
