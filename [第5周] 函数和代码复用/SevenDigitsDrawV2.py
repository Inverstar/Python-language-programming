#SevenDigitsDrawV2.py
import turtle, time

def drawGap_V2(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawLine_V2(draw):   #绘制单段数码管
    drawGap_V2()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap_V2()
    turtle.right(90)

def drawDigit_V2(d): #根据数字绘制七段数码管
    drawLine_V2(True) if d in [2,3,4,5,6,8,9] else drawLine_V2(False)
    drawLine_V2(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine_V2(False)
    drawLine_V2(True) if d in [0,2,3,5,6,8,9] else drawLine_V2(False)
    drawLine_V2(True) if d in [0,2,6,8] else drawLine_V2(False)
    turtle.left(90)
    drawLine_V2(True) if d in [0,4,5,6,8,9] else drawLine_V2(False)
    drawLine_V2(True) if d in [0,2,3,5,6,7,8,9] else drawLine_V2(False)
    drawLine_V2(True) if d in [0,1,2,3,4,7,8,9] else drawLine_V2(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawDate_V2(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial", 18, "normal"))
        else:
            drawDigit_V2(eval(i))

def SevenDigitsDrawV2():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
#    drawDate_V2('2018-10=10+')
    drawDate_V2(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
    turtle.done()

SevenDigitsDrawV2()