#SevenDigitsDrawV1.py
import turtle
def drawLine_V1(draw):   #绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit_V1(digit): #根据数字绘制七段数码管
    drawLine_V1(True) if digit in [2,3,4,5,6,8,9] else drawLine_V1(False)
    drawLine_V1(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine_V1(False)
    drawLine_V1(True) if digit in [0,2,3,5,6,8,9] else drawLine_V1(False)
    drawLine_V1(True) if digit in [0,2,6,8] else drawLine_V1(False)
    turtle.left(90)
    drawLine_V1(True) if digit in [0,4,5,6,8,9] else drawLine_V1(False)
    drawLine_V1(True) if digit in [0,2,3,5,6,7,8,9] else drawLine_V1(False)
    drawLine_V1(True) if digit in [0,1,2,3,4,7,8,9] else drawLine_V1(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20) 
def drawDate_V1(date):  #获得要输出的数字
    for i in date:
        drawDigit_V1(eval(i))  #通过eval()函数将数字变为整数
def SevenDigitsDrawV1():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate_V1('20181010')
    turtle.hideturtle()
    turtle.done()

SevenDigitsDrawV1()