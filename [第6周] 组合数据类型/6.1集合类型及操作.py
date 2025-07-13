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
        """
    # 集合类型及操作  

    ## 集合类型定义  

    ### 集合是多个元素的无序组合  

    - 集合类型与数学中的集合概念一致  
    - 集合元素之间无序，每个元素唯一，不存在相同元素  
    - 集合元素不可更改，不能是可变数据类型  
    - 集合用大括号{}表示，元素间用逗号分隔  
    - 建立集合类型用{}或set()  
    - 建立空集合类型，必须使用set()
    """
    )
    return


@app.cell
def _():
    A = {"","python",321,("python",123)}
    print(A)
    B = set("python123321")
    print(B)
    C = {"","python",321,"python",123}
    print(C)
    D1 = {} #空字典
    D2 = set() #空集合
    print(D1,D2)
    return


@app.cell
def _(mo):
    mo.md(
        r"""

    ## 集合操作符  

    ### 集合间操作
    """
    )
    return


@app.cell
def _():
    S = {1,2,3,4,5,'a'}
    T = {1,2,3,4,5,'b'}

    print(S|T) #并
    print(S-T) #差
    print(S&T) #交
    print(S^T) #补
    print(S<=(T|S)) #判断S是不是T的子集

    S|=T
    print(S)
    S-=T
    print(S)
    S&=T
    print(S)
    S^=T
    print(S)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## 集合处理方法  

    ## 集合类型应用场景  
    """
    )
    return


if __name__ == "__main__":
    app.run()
