import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
    # 序列类型及操作  

    ## 序列类型定义  

    ### 序列是具有先后关系的一组元素  

    - 序列是一维元素向量，元素类型可以不同   
    - 类似数学元素序列：$S_0$, $S_1$, ... , $S_{n-1}$  
    - 元素间由序号引导，通过下标访问序列的特定元素  

    ### 序列是一个基类类型  

    - 序列类型
        - 字符串类型
        - 元组类型
        - 列表类型

    ### 序号的定义
    """
    )
    return


@app.cell
def _():
    list = ["BIT",3.1425,1024,(2,3),["中国",9]]
    for i in range(5):
        print(list[i],i)
    for i in range(-5,0):
        print(list[i],i)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## 序列处理函数及方法

    ### 序列类型通用操作符

    x in s              # 如果x是序列s的元素，返回True，否则返回False  
    x not in s          # 如果x不是序列s的元素，返回True，否则返回False  
    s + t               # 连接两个序列s和t  
    s * n 或 n * s       # 将序列s复制n次   
    s[i]                # 索引，返回s中的第i个元素，i是序列的序号  
    s[i:j]或s[i:j:k]     # 切片，返回序列s中从第i个到第j个(不含)元素，以k为步长的子序列  
    s[::-1] #倒序  

    ### 序列类型通用函数和方法

    # 序列的常用方法
    len(s)          # 返回序列s的长度，即元素个数  
    min(s)          # 返回序列s的最小元素，s中元素需要可比较  
    max(s)          # 返回序列s的最大元素，s中元素需要可比较  
    s.index(x)      # 返回序列s中第一次出现元素x的位置  
    s.index(x,i,j)  # 返回序列s从i开始到j位置中第一次出现元素x的位置  
    s.count(x)      # 返回序列s中出现x的总次数  

    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## 元组类型及操作

    S.add(x) #如果x不在序列s中，将x增加到s  
    S.discard(x) #移除S中元素x，如果x不在序列S中，不报错  
    S.remove(x) #移除s中元素x，如果x不在序列s中，产生KeyError异常  
    S.clear() #移除s中所有元素  
    S.POP() #随机返回s的一个元素，更新s，若s为空产生KeyError异常  

    S.copy() #返回序列s的一个副本  
    len(S) #返回序列s的元素个数  
    x in S #判断s中元素×，x在序列s中，返回True,否则返回False
    x not in S #判断s中元素×，x不在序列s中，返回True,否则返回False
    set(x) #将其他类型变量×转变为序列类型
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## 列表类型及操作

    ## 序列类型应用场景
    """
    )
    return


if __name__ == "__main__":
    app.run()
