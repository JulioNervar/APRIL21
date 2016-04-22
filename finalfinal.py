from math import pi
total = [];
def multiplier(count,number,number1):
    total.append(number) if count ==1 else multiplier(count-1,number+number1,number1)
def c_area(count,number,number1):
    multiplier(number, pi, pi) if count == 1 else c_area(count-1,number+number1,number1)
def triangle(count,number,number1):
    multiplier(number, 0.5, 0.5) if count == 1 else triangle(count-1,number+number1,number1)
def square():
    l = int(raw_input("Enter the length of the side of the SQUARE : "))
    multiplier(l, l, l)
square()
def rectangle():
    height = int(raw_input("Enter the length of the RECTANGLE : "))
    length = int(raw_input("Enter the height of the RECTANGLE : "))
    multiplier(height, length, length)
rectangle()
def circle():
    r = int(raw_input("Enter the radius of the CIRCLE : "))
    c_area(r, r, r)
circle()
def tri():
    t = int(raw_input("Enter the base of the TRIANGLE : "))
    h = int(raw_input("Enter the height of the TRIANGLE : "))
    triangle(t, h, h)
tri()

taas = max(total)
high = ""
if total[0] == taas:
    high = "SQUARE"
elif total[1] == taas:
    high = "RECTANGLE"
elif total[2] == taas:
    high = "CIRCLE"
elif total[3] == taas:
    high = "TRIANGLE"

def boom():
    choco = raw_input("YOU ONLY HAVE 2 GUESSES. ENTER WHICH SHAPE HAS THE HIGHEST AREA : ")
    if choco.upper() == high :
        print "YEHEY YOU GOT IT!"
    elif choco.upper() != high :
        print "WRONG."
        choco = raw_input("ENTER YOUR LAST GUESS : ")
        if choco.upper() == high :
            print "YEHEY YOU GOT IT!"
        else:
            print "YOU LOSE. THE CORRECT ANSWER IS " + high
boom()









