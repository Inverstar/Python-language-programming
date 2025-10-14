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
    # 文件的使用  

    ## 文件的类型  

    ## 文件的打开和关闭  
    ## 文件内容的读取  
    ## 数据的文件写入  

    """
    )
    return


if __name__ == "__main__":
    app.run()
