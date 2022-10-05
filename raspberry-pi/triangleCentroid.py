import math
import board
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import displayio
import adafruit_displayio_ssd1306
import busio

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
landHere = 0
while True:
    try:

        points = [[-50,-17,-57,12,-22,-7],[28,-14,60,-7,54,18],[45,30,51,-1,18,6],[5,5,19,15,22,10]]

        for x in range(len(points)):
            triangleDistance = triangleCentroid(points[x][0], points[x][1], points[x][2], points[x][3], points[x][4], points[x][5], points[x][5])
            triAreaValue = triangleArea(points[x][0], points[x][1], points[x][2], points[x][3], points[x][4], points[x][5], points[x][5])
            if triangleDistance > landHere and triAreaValue > 100:
                landHere = triangle
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
        
    except:
        print("Please input valid coordinates (remember format x,y)")