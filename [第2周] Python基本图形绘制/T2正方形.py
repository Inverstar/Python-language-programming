# import turtle

# # 画一个正中心在(0,0)，边长为100的正方形
# turtle.penup()
# turtle.goto(0, 0)
# turtle.dot(10, "red") 
# turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))
# turtle.penup()
# turtle.goto(-50, -50)  # 移动到左下角
# turtle.setheading(0)

# turtle.pendown()
# for _ in range(4):
#     turtle.fd(100)
#     turtle.write(str(turtle.pos()), align="right", font=("Arial", 10, "normal"))
#     turtle.left(90)

# turtle.done()

# turtle.write(str(turtle.pos()), align="left", font=("Arial", 10, "normal"))

#RectDraw.py
import turtle as t
t.pensize(2)
for i in range(4):
    t.fd(150)
    t.left(90)

t.done()