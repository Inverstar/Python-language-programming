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
    # 代码复用与函数递归  

    ## 代码复用与模块化设计  

    ### 把代码当成资源进行抽象  

    - 代码资源化：程序代码是一种用来表达计算的资源  
    - 代码抽象化：使用函数等方法对代码赋予更高级别的定义  
    - 代码复用：同一份代码在需要时可以被重复使用

    ### 函数和对象是代码复用的两种主要形式  

    - 函数：将代码命名在代码层面建立了初步抽象  
    - 对象：属性和方法<a\>.<b\> 和 <c\>.<d\>() 在函数之上再次组织进行抽象

    ### 分而治之  

    - 通过函数或对象封装将程序划分为模块及模块间的表达  
    - 具体包括：主程序、子程序子程序间关系  
    - 分而治之：一种分而治之、分层抽象、体系化的设计思想  

    ### 紧耦合 松耦合  

    - 紧耦合：两个部分之间交流很多，无法独立存在  
    - 松耦合：两个部分之间交流较少，可以独立存在  
    - 模块内部紧耦合、模块之间松耦合  

    ## 函数递归的理解  

    ### 递归的定义

    函数定义中调用函数自身的方式  

    - 链条：计算过程存在递归链条  
    - 基例：存在一个或多个不需要再次递归的基例  

    ### 类似数学归纳法  

    数学归纳法  

    - 证明当n取第一个值时$n_0$命题成立  
    - 假设当$n_k$时命题成立，证明当n=$n_{k+1}$时命题也成立  
    - 递归是数学归纳法思维的编程体现


    ## 函数递归的调用过程  

    ### 递归的实现
    """
    )
    return


@app.cell
def fact():
    def fact(n):
        if n == 0 : 
            return 1
        else :
            return n*fact(n-1)

    print(fact(3))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    函数 + 分支语句

    - 递归本身是一个函数，需要函数定义方式描述  
    - 函数内部，采用分支语句对输入参数进行判断  
    - 基例和链条，分别编写对应代码
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## 函数递归实例解析

    ### 字符串反转
    """
    )
    return


@app.cell
def _():
    s = "012345"
    print(s[::-1])
    def rvs(s): #函数 + 分支结构
        if s == "":
            return s #递归基例
        else:
            return rvs(s[1:])+s[0] #递归链条
    print(rvs(s))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### 斐波那契数列

    $F(n) = \begin{cases} 1 & n = 1 \\ 1 & n = 2 \\F(n-1) + F(n-2) & otherwise \end{cases}$
    """
    )
    return


@app.function
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)


@app.cell
def _(mo):
    mo.md(r"""### 汉诺塔""")
    return


@app.cell
def _():
    count = 0
    def hanoi(n, src, dst, mid):
        global count
        if n == 1:
            print("{}:{}->{}".format(1,src,dst))
            count += 1
        else:
            hanoi(n-1, src, mid, dst)
            print("{}:{}->{}".format(n,src,dst))
            count += 1
            hanoi(n-1, mid, dst, src)
    return


if __name__ == "__main__":
    app.run()
