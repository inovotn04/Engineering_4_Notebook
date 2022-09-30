import math
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
    except:
        print("Please input valid coordinates (remember format x,y)")