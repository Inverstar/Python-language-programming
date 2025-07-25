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
    # 1.1程序设计基本方法

    ## Moore's Law

    摩尔定律-该预测使得计算机成为长期指数级发展的产业

    ## 编译与解释

    编译器 compiler 一次性翻译 静态语言  
    解释器 interpreter 实时翻译 脚本语言

    ## IPO

    ### I Input 输入  

    - 文件输入（读取文件）  
    - 网络输入  
    - 控制台输入  
    - 交互界面输入  
    - 内部参数输入等

    ### P Process 处理  

    - 处理方法统称算法

    ### O Output 输出  

    - 控制台输出  
    - 图形输出  
    - 文件输出  
    - 网络输出  
    - 内部变量输出等  

    ## 计算思维：抽象交互关系、自动化执行，区别数学的逻辑思维与物理的实证思维
    """
    )
    return


if __name__ == "__main__":
    app.run()
