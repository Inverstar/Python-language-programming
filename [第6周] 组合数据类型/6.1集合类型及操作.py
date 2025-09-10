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
    return (S,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## 集合处理方法  

    S.add(x) #如果x不在集合s中，将x增加到s  
    S.discard(x) #移除S中元素x，如果x不在集合S中，不报错  
    S.remove(x) #移除s中元素x，如果x不在集合s中，产生KeyError异常  
    S.clear() #移除s中所有元素  
    S.POP() #随机返回s的一个元素，更新s，若s为空产生KeyError异常  

    S.copy() #返回集合s的一个副本  
    len(S) #返回集合s的元素个数  
    x in S #判断s中元素×，x在集合s中，返回True,否则返回False
    x not in S #判断s中元素×，x不在集合s中，返回True,否则返回False
    set(x) #将其他类型变量×转变为集合类型
    """
    )
    return


@app.cell
def _(S):
    S.add(7) #添加7
    X = S.copy()
    len(X)
    print(7 in X)
    S.discard(7) #移除7，不存在不报错
    print(7 not in S)
    # 提示用户（若不存在则输出信息）
    try:
        S.remove(7) #移除7，若7不存在报错
    except (ValueError, KeyError) as e:
        print(f"移除元素失败: {e}")
    except Exception as e:
        print(f"错误类型: {type(e)}")
        print(f"错误信息: {e}")
    S.clear() #移除所有元素
    try:
        S.pop() #随机返回一个元素，若S为空报错
    except (ValueError, KeyError) as e:
        print(f"移除元素失败: {e}")
    except Exception as e:
        print(f"错误类型: {type(e)}")
        print(f"错误信息: {e}")
    x = [7]
    y = set(x)
    print(x,y)

    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## 集合类型应用场景

    ### 包含关系比较

    对元素是否存在做判断

    ### 数据去重
    """
    )
    return


@app.cell
def _():
    ls = [7,7]
    s = set(ls)
    lt = list(s)
    print(lt)
    return


if __name__ == "__main__":
    app.run()
