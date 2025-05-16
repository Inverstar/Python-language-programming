#PythonDraw2.py
import turtle #引入turtle模块海龟库
# turtle.setup(650, 350, 200, 200) #设置窗口大小和位置
#turtle.setup(width, height, startx, starty)分别表示窗口的宽度、高度、左上角x坐标和y坐标
turtle.setup(2560, 1080) #startx, starty可以省略
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)   # 设置海龟的方向 
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()