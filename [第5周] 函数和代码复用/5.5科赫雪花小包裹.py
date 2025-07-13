import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # 科赫雪花小包裹  

    ## 科赫雪花  

    ### 分形几何-科赫曲线也叫雪花曲线
    """
    )
    return


@app.cell
def fact():
    #KochDrawV1.py
    import turtle
    def koch(size, n):
        if n == 0:
            turtle.fd(size)
        else:
            for angle in [0, 60, -120, 60]:
               turtle.left(angle)
               koch(size/3, n-1)
    def main():
        turtle.setup(800,400)
        turtle.penup()
        turtle.goto(-300, -50)
        turtle.pendown()
        turtle.pensize(2)
        koch(600,3)     # 0阶科赫曲线长度，阶数
        turtle.hideturtle()
        #turtle.done()
        return 0
    main()
    return (turtle,)


@app.cell
def _(turtle):
    #KochDrawV2.py
    #import turtle
    def koch_V2(size, n):
        if n == 0:
            turtle.fd(size)
        else:
            for angle in [0, 60, -120, 60]:
               turtle.left(angle)
               koch_V2(size/3, n-1)
    def main_V2():
        turtle.setup(600,600)
        turtle.penup()
        turtle.goto(-200, 100)
        turtle.pendown()
        turtle.pensize(2)
        level = 5      # 3阶科赫雪花，阶数
        koch_V2(400,level)     
        turtle.right(120)
        koch_V2(400,level)
        turtle.right(120)
        koch_V2(400,level)
        turtle.hideturtle()
        turtle.done()
        return 0
    main_V2()

    return


if __name__ == "__main__":
    app.run()
