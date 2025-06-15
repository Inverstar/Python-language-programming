import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # 七段代码管绘制  

    ## 基本思路  

    - 步骤1：绘制单个数字对应的数码管  
        - 七段数码管由7个基本线条组成  
        - 七段数码管可以有固定顺序  
        - 不同数字显示不同的线条  
    - 步骤2：获得一串数字，绘制对应的数码管  
    - 步骤3：获得当前系统时间，绘制对应的数码管  
        - 使用time库获得系统当前时间  
        - 增加年月日标记  
        - 年月日颜色不同

    ## 思维方法  

    - 模块化思维：确定模块接口，封装功能  
    - 规则化思维：抽象过程为规则，计算机自动执行  
    - 化繁为简：将大功能变为小功能组合，分而治之

    ## 举一反三  

    - 绘制带小数点的七段数码管  
    - 带刷新的时间倒计时效果  
    - 绘制高级的数码管
    """
    )
    return


@app.cell
def _():
    #SevenDigitsDrawV1.py
    import turtle, time
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
        #turtle.done()
        return 0

    SevenDigitsDrawV1()
    return time, turtle


@app.cell
def _(time, turtle):
    #SevenDigitsDrawV2.py
    #import turtle, time
    #import time

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
        #turtle.done()
        time.sleep(3)
        turtle.bye()
        return 0

    SevenDigitsDrawV2()

    return


if __name__ == "__main__":
    app.run()
