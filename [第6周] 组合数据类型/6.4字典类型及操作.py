import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # 字典类型及操作

    ## 字典类型定义

    - 映射是一种键(索引)和值(数据)的对应
    - 字典类型是“映射”的体现
     - 键值对：键是数据索引的扩展
     - 字典是键值对的集合，键值对之间无序
     - 采用大括号{}和dict()创建，键值对用冒号：表示
    """
    )
    return


@app.cell
def _():
    d={"中国":"北京","美国":"华盛顿","法国":"巴黎"}
    print(d)
    print(d["中国"])
    d["中国"] = "深圳"
    print(d)
    de = {};
    print(type(de))
    return (d,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 字典处理函数及方法

    | 函数或方法          | 描述                                            |
    | ------------------- | ----------------------------------------------- |
    | del d[k]            | 删除字典d中键k对应的数据值                      |
    | k in d              | 判断键k是否在字典d中，如果在返回True，否则False |
    | d.keys()            | 返回字典d中所有的键信息                         |
    | d.values()          | 返回字典d中所有的值信息                         |
    | d.items()           | 返回字典d中所有的键值对信息                     |
    | d.get(k, <default>) | 键k存在,则返回相应值，不在则返回<default>值     |
    | d.pop(k, <default>) | 键k存在，则取出相应值，不在则返回<default>值    |
    | d.popitem()         | 随机从字典d中取出一个键值对，以元组形式返回     |
    | d.clear()           | 删除所有的键值对                                |
    | len(d)              | 返回字典d中元素的个数                           |
    """
    )
    return


@app.cell
def _(d):
    print("中国" in d)
    print(d.keys())
    print(d.values())

    print(d.get("中国","不存在"))
    print(d.get("巴基斯坦","不存在"))
    print(d.popitem())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 字典类型应用场景  

    - 映射关系采用键值对表达
    - 字典类型使用0和dict0创建，键值对之间用：分隔
    - d[key]方式既可以索引l，也可以赋值
    - 字典类型有一批操作方法和函数，最重要的是.get()
    """
    )
    return


if __name__ == "__main__":
    app.run()
