import math
import board
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import displayio
import adafruit_displayio_ssd1306
import busio
import time #import libraries

displayio.release_displays() #This is something you need to do for the LCD displays 
sda_pin = board.GP14
scl_pin = board.GP15 #defines i2c pins
i2c = busio.I2C(scl_pin, sda_pin) #inits i2c

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP19) #inits display
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)



def triangleArea(x1, y1, x2, y2, x3, y3): #Creates function with 6 variables as input
    AreaValue = (abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))/2 #calculates triangle area
    print(AreaValue) #prints it
    return(AreaValue) #also returns it
def triangleCentroid(x1,y1, x2, y2, x3, y3): #creates another function
    centroidValueX = (x1 + x2 + x3)/3 #Calculates first (x) variable of centroid
    centroidValueY = (y1 + y2 + y3)/3 #Calculates second (y) variable of centroid
    distanceVal = math.sqrt(((centroidValueX)**2)+((centroidValueY)**2)) #Calculates distance from center
    print(distanceVal)
    return(distanceVal)
landHere = 10000 #Just made an arbitrarily large variable to compare to distance values
try:
    points = [[-2,-30,-19,-8,-44,-18],[7,-14,60,-7,33,-6],[5,5,-8,9,0,-6],[63,30,60,19,29,16]] #Defines list of lists which has coordinates in them
    for x in range(len(points)): #loops through based on the number of points given
        triangleDistance = triangleCentroid(points[x][0], points[x][1], points[x][2], points[x][3], points[x][4], points[x][5]) #Calls the triangleCentroid function to find distance of given coordinates
        triAreaValue = triangleArea(points[x][0], points[x][1], points[x][2], points[x][3], points[x][4], points[x][5]) #Calls triangleArea to find the triangle area
        if triangleDistance < landHere and triAreaValue > 100: #If the given triangle satisfies the parameters it will replace the last one as the best triangle
            landHere = triangleDistance
            bestPoints = points[x]
            bestArea = triAreaValue
        
        c1 = int(points[x][0]+64)
        d1 = int(-points[x][1]+32)

        c2 = int(points[x][2]+64)
        d2 = int(-points[x][3]+32)                 #These few lines create the triangle points to display on the display

        c3 = int(points[x][4]+64)
        d3 = int(-points[x][5]+32)

        splash = displayio.Group() #This is another weird LCD display thing

        hline = Line(0, 32, 128, 32, color=0xFFFF00) #Creates the line I think
        splash.append(hline) #Adds it to the weird LCD thing

        hline = Line(64, 64, 64, 0, color=0xFFFF00) #Another line
        splash.append(hline) #Added

        circle = Circle(64, 32, 2, outline=0xFFFF00) #Creates circle point for the center
        splash.append(circle) #And adds it as well


        triangle = Triangle(c1, d1, c2, d2, c3, d3, outline=0xFFFF00) #Creates the triangle with the given points
        splash.append(triangle) #And adds it 
        display.show(splash) #Completes the display I think so it shows everything
        time.sleep(1)
    print(f"The closest suitable landing area has vertices ({bestPoints[0]}, {bestPoints[1]}) ({bestPoints[2]}, {bestPoints[3]}) ({bestPoints[4]}, {bestPoints[5]}). The area is {bestArea} km2 and the centroid is {landHere} km away from base.")
    triangle = Triangle((bestPoints[0]+64), (-bestPoints[1]+32), (bestPoints[2]+64), (-bestPoints[3]+32), (bestPoints[4]+64), (-bestPoints[5]+32), outline=0xFFFF00)
    splash.append(triangle) #Aboves two lines take the best triangle out of all them, and prints a message notifying the user of it, as well as displays it on the LCD
    display.show(splash)
    while True:
        time.sleep(1) #I put this here so it would permanently display the triangle

except Exception as e:
    print(e) #Prints error code if there is error :)