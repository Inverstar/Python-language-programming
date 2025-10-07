import marimo

__generated_with = "0.15.3"
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

    ### 元组类型定义

    #### 元组是序列类型的一种扩展类型

    - 元组是一种序列类型，一旦创建不能被修改  
    - 使用小括号()或tuple()创建，元素间用逗号，分隔  
    - 可以使用或不使用小括号

    ### 元组类型操作

    #### 元组继承序列类型的全部通用操作

    - 元组继承序列类型的全部通用操作
    - 元组创建后不能修改，因此没有特殊操作
    - 使用或不使用小括号
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## 列表类型及操作

    ### 列表是序列类型的一种扩展，十分常用  

    - 列表是一种序列类型，创建后可以随意被修改  
    - 使用方括号[]或list()创建，元素间用逗号,分隔  
    - 列表中各元素类型可以不同，无长度限制
    """
    )
    return


@app.cell
def _():
    ls = ["a","b"]
    print(ls)
    lt = ls
    print(lt)
    ls[0] = "c"
    print(lt) #方括号创建列表，赋值仅传递引用，所以ls变了，lt也会变
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### 列表类型操作函数和方法

    ls[i] = x          # 替换列表ls第i个元素为x  
    ls[i:j:k] = lt     # 用列表lt替换ls切片后所对应元素子列表  
    del ls[i]          # 删除列表ls中第i个元素  
    del ls[i:j:k]      # 删除列表ls中从第i到j以k为步长的元素  
    ls += lt           # 更新列表ls，将列表lt的元素添加到列表ls中  
    ls *= n            # 更新列表ls，将其元素重复n次  

    ls.append(x)      # 在列表ls最后增加一个元素x  
    ls.clear()        # 删除列表ls中所有元素  
    ls.copy()         # 生成一个新列表，复制ls中所有元素  
    ls.insert(i,x)    # 在列表ls的第i个位置增加元素x  
    ls.pop(i)         # 将列表ls中第i个位置元素取出并删除该元素  
    ls.remove(x)      # 将列表ls中出现的第一个元素x删除  
    ls.reverse()      # 将列表ls中的元素反转
    """
    )
    return


@app.cell
def _():
    import random
    random_num = random.randint(0, 1)
    k = [1,2,3,4,5]
    if random_num == 1:
        k = [1]
    print(k)
    squares = [x**2 for x in range(10)]
    print(squares)
    #左右列表的数量要一致才能成功
    try:
        squares[1:10:2] = k  # 尝试替换切片
    except ValueError as e:
        print(f"值错误：可能是替换序列长度不匹配, {e},k={k}")
    except TypeError as e:
        print(f"类型错误：k可能不是可迭代对象, {e},k={k}")
    except Exception as e:
        print(f"其他错误：{type(e).__name__}, {e},k={k}")
    print(squares[1:10:2])
    print(squares)
    s = squares.copy()
    squares.reverse()
    print(s,squares)
    # 使用列表实现栈的功能
    stack = []      # 创建空栈

    # 入栈操作 (push)
    stack.append(1)  # [1]
    stack.append(2)  # [1, 2]
    stack.append(3)  # [1, 2, 3]

    print(f"入栈后：{stack}")  # 入栈后：[1, 2, 3]

    # 出栈操作 (pop)
    last = stack.pop()  # 弹出 3
    print(f"出栈元素：{last}")  # 出栈元素：3
    print(f"当前栈：{stack}")   # 当前栈：[1, 2]

    # 查看栈顶元素
    top = stack[-1]     # 获取栈顶元素但不删除
    print(f"栈顶元素：{top}")   # 栈顶元素：2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 序列类型应用场景

    - 元组用于元素不改变的应用场景，更多用于固定搭配场景  
    - 列表更加灵活，它是最常用的序列类型  
    - 最主要作用：表示一组有序数据，进而操作它们
    """
    )
    return


@app.cell
def _():
    #元素遍历
    stack1 = [1,2]
    for i1 in stack1:
        print(i1)
    #数据转换
    stack1 = tuple(stack1)
    print(stack1)
    return


if __name__ == "__main__":
    app.run()
