import board
import time
import digitalio #Imports necessary libraries


print("Countdown time") #You know what this line does
x = 10 #Sets x variable to 10 to work the for loop
for x in range (10, -1, -1): #for loop, counts down from 10, until it reaches -1
 print(x) #prints countdown
 time.sleep(1)
print("Liftoff") 
