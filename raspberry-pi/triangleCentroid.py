import math
import board
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import displayio
import adafruit_displayio_ssd1306
import busio
import time

displayio.release_displays()
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP19)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)



def triangleArea(x1, y1, x2, y2, x3, y3):
    AreaValue = (abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))/2
    return(AreaValue)
def triangleCentroid(x1,y1, x2, y2, x3, y3):
    centroidValueX = (x1 + x2 + x3)/3
    centroidValueY = (y1 + y2 + y3)/3
    distanceVal = math.sqrt(((centroidValueX - 64)**2)+((centroidValueY-32)**2))
    return(distanceVal)
landHere = 10000
try:
    points = [[-2,-30,-19,-8,-44,-18],[7,-14,60,-7,33,-6],[5,5,-8,9,0,-6],[63,30,60,19,29,16]]
    for x in range(len(points)):
        triangleDistance = triangleCentroid(points[x][0], points[x][1], points[x][2], points[x][3], points[x][4], points[x][5])
        triAreaValue = triangleArea(points[x][0], points[x][1], points[x][2], points[x][3], points[x][4], points[x][5])
        if triangleDistance < landHere and triAreaValue > 100:
            landHere = triangleDistance
            bestPoints = points[x]
            bestArea = triAreaValue
        
        c1 = int(points[x][0])
        d1 = int(points[x][1])

        c2 = int(points[x][2])
        d2 = int(points[x][3])

        c3 = int(points[x][4])
        d3 = int(points[x][5])

        splash = displayio.Group()

        hline = Line(0, 32, 128, 32, color=0xFFFF00)
        splash.append(hline)

        hline = Line(64, 64, 64, 0, color=0xFFFF00)
        splash.append(hline)

        circle = Circle(64, 32, 2, outline=0xFFFF00)
        splash.append(circle)


        triangle = Triangle(c1, d1, c2, d2, c3, d3, outline=0xFFFF00)
        splash.append(triangle)
        display.show(splash)
        time.sleep(1)
    print(f"The closest suitable landing area has vertices ({bestPoints[0]}, {bestPoints[1]}) ({bestPoints[2]}, {bestPoints[3]}) ({bestPoints[4]}, {bestPoints[5]}). The area is {bestArea} km2 and the centroid is {landHere} km away from base.")
    triangle = Triangle(bestPoints[0], bestPoints[1], bestPoints[2], bestPoints[3], bestPoints[4], bestPoints[5], outline=0xFFFF00)
    splash.append(triangle)
    display.show(splash)
    while True:
        time.sleep(1)

except Exception as e:
    print(e)