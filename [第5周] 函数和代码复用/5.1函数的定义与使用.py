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
        # 函数的定义与使用
    
        ## 函数的理解与定义
    
        函数是一段代码的表示
    
        - 函数是一段具有特定功能的、可重用的语句组
        - 函数是一种功能的抽象，一般函数表达特定功能
        - 两个作用：降低编程难度代码复用
        - def <函数名>(参数):
          -  <函数体>
          -  return <返回值>
        """
    )
    return


@app.cell
def _():
    #计算n的阶乘
    def factorial(n):
        s = 1
        for i in range(1, n + 1):
            s *= i
        return s

    f = factorial(5)
    print(f)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 函数的使用及调用过程
    
        调用是运行函数代码的方式  
    
        - 调用时要给出实际参数  
        - 实际参数替换定义中的参数  
        - 函数调用后得到返回值
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 函数的参数传递
    
        函数可以有参数，也可以没有，但必须保留括号  
    
        ### 可选参数传递  
    
        函数定义时可以为某些参数指定默认值，构成可选参数
        """
    )
    return


@app.cell
def _():
    # 本函数的m就是可选参数
    def fact(n, m=1):
        s = 1
        for i in range(1, n + 1):
            s *= i
        return s / m

    f5_2 = fact(5, 2)
    print(f5_2)
    f5 = fact(5)
    print(f5)
    return (fact,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ### 可变参数传递  
    
        函数定义时可以设计可变数量参数，既不确定参数总数量
        """
    )
    return


@app.cell
def _():
    # 本函数的b就是可变参数
    def factb(n, *b):
        s = 1
        for i in range(1, n + 1):
            s *= i
        for item in b:
            s *= item
        return s

    f5_3 = factb(5, 3)
    print(f5_3)
    f5_2_3 = factb(5, 2, 3)
    print(f5_2_3)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### 参数传递的两种方式  
    
        参数可以按照位置或名称方式传递，推荐名称，准确
        """
    )
    return


@app.cell
def _(fact):
    fact_n_m = fact(10, 5) #位置传递
    fact_m_n = fact(m = 5, n = 10) #名称传递
    print(fact_n_m, fact_m_n)

    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 函数的返回值
    
        函数可以返回0个或多个结果  
    
        - return保留字用来传递返回值  
        - 函数可以有返回值，也可以没有，可以有return，也可以没有  
        - return可以传递0个返回值，也可以传递任意多个返回值
        """
    )
    return


@app.cell
def _(fact):
    #多个返回值时，返回类型是元组，可以用同等数量的变量接收
    fact_return = fact(5, 2), fact(5)
    print(fact_return)
    #也可以用一个变量接收，返回值是元组
    fact_return2 = fact(5, 2)
    print(fact_return2)

    def fact_return_tuple(n, m=1):
        s = 1
        for i in range(1, n + 1):
            s *= i
        return s, s / m

    fact_return3 = fact_return_tuple(5, 2)
    print(fact_return3)
    return_value1, return_value2 = fact_return_tuple(5, 2)
    print(return_value1, return_value2)

    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 局部变量全局变量  
    
        规则1：局部变量全局变量是不同变量 
    
        - 局部变量是函数内部的占位符，与全局变量可能重名但不同  
        - 函数运算结束后，局部变量被释放  
        - 可以使用global保留字在函数内部使用全局变量
        """
    )
    return


@app.cell
def _():
    n,s = 10, 100
    def fact_global(n):
        global s
        for i in range(1, n + 1):
            s *= i
        return s #s是全局变量，已被函数修改

    print(fact_global(n),s)

    return


@app.cell
def _(mo):
    mo.md(r"规则2：局部变量为组合数据类型且未创建，等同于全局变量")
    return


@app.cell
def _():
    ls = ["first", "second", "third"] # ls是全局变量，函数修改后会影响全局变量
    def fact_list(n):
        for i in range(1, n + 1):
            ls.append(i) #局部变量ls为组合数据类型且未创建，等同于全局变量
        return ls

    print(fact_list(5))  # ls被函数修改，返回值是修改后的列表
    print(ls)  # ls被函数修改，直接打印列表

    return


@app.cell
def _(mo):
    mo.md(
        r"""
        使用规则  
    
        - 基本数据类型，无论是否重名，局部变量与全局变量不同  
        - 可以通global保留字在函数内部声明全局变量  
        - 组合数据类型，如果局部变量未真实创建，则是全局变量
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## lambda函数  
    
        lambda函数返回函数名作为结果  
    
        - lambda函数是一种匿名函数，即没有名字的函数  
        - 使用lambda保留字定义，函数名是返回结果  
        - lambda函数用于定义简单的、能够在一行内表示的函数
        """
    )
    return


@app.cell
def _():
    f_lambda = lambda x,y: x + y  # lambda函数
    print(f_lambda(5, 3))  # 调用lambda函数
    return


if __name__ == "__main__":
    app.run()
