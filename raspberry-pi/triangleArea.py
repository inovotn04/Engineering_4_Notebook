import math

def tri_area(x1, y1, x2, y2, x3, y3):
    niceAreaValue = (abs(x1(y2-y3)+x2(y3-y1)+x3(y1-y2)))/2
    niceAreaString = str(niceAreaValue)

txt1 = input("Input coord set 1 (x,y)")
set1 = txt1.split(",")

x1 = float(set1[0])
y1 = float(set1[1])

txt2 = input("Input coord set 1 (x,y)")
set2 = txt2.split(",")

x2 = float(set2[0])
y2 = float(set2[1])

txt3 = input("Input coord set 1 (x,y)")
set3 = txt3.split(",")

x3 = float(set3[0])
y3 = float(set3[1])

tri_area(x1, y1, x2, y2, x3, y3)
print(niceAreaString)