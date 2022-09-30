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



def tri_area(x1, y1, x2, y2, x3, y3):
    niceAreaValue = (abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))/2
    print(f"The area of the triangle with vertices ({x1}, {y1}), ({x2}, {y2}), ({x3}, {y3}) is {niceAreaValue}")
while True:
    try:
        txt1 = input("Input coord set 1 (x,y)")
        set1 = txt1.split(",")

        a1 = float(set1[0])
        b1 = float(set1[1])

        txt2 = input("Input coord set 2 (x,y)")
        set2 = txt2.split(",")

        a2 = float(set2[0])
        b2 = float(set2[1])

        txt3 = input("Input coord set 3 (x,y)")
        set3 = txt3.split(",")

        a3 = float(set3[0])
        b3 = float(set3[1])

        tri_area(a1, b1, a2, b2, a3, b3)

        c1 = int(a1)
        d1 = int(b1)

        c2 = int(a2)
        d2 = int(b2)

        c3 = int(a3)
        d3 = int(b3)

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