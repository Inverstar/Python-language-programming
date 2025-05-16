import turtle

# turtle空间坐标体系
# turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))
# turtle.goto(100, 100)  
# turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))
# turtle.goto(100, -100)
# turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))
# turtle.goto(-100, -100)
# turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))
# turtle.goto(-100, 100)
# turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))
# turtle.goto(0, 0)

# turtle.bk(100)  # 向后移动100像素
# turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))
# turtle.circle(100)  # 画一个半径为100的圆
# turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))
# turtle.fd(100)  # 向前移动100像素
# turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))
# turtle.circle(100, 180)  # 画一个半径为100的圆，弧度为180度

# turtle角度坐标体系

# turtle.seth(0)  # 设置海龟的方向为0度
# turtle.circle(100)  # 画一个半径为100的圆
# turtle.seth(90)  # 设置海龟的方向为90度 

# turtle.left(90)  # 向左转90度
# turtle.fd(100)  # 向前移动100像素
# turtle.right(90)  # 向右转90度
# turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))
# turtle.fd(100)  # 向前移动100像素


# 画一个正中心在(0,0)，边长为100的正方形
turtle.penup()
turtle.goto(0, 0)
turtle.dot(10, "red") 
turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))
turtle.penup()
turtle.goto(-50, -50)  # 移动到左下角
turtle.setheading(0)

turtle.pendown()
for _ in range(4):
    turtle.fd(100)
    turtle.write(str(turtle.pos()), align="right", font=("Arial", 10, "normal"))
    turtle.left(90)

turtle.done()

turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))