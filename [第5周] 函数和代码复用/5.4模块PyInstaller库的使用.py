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
    # 模块PyInstaller库的使用  

    ## PyInstaller库基本介绍  

    ### 将.py源代码转换成无需源代码的可执行文件  

    - .py文件  
    - PyInstaller  
    - Windows（exe文件）、Linux、Mac OS X

    ### PyInstaller库是第三方库  

    - 官方网站：http://www.pyinstaller.org  
    - 第三方库：使用前需要额外安装  
    - 安装第三方库需要使用pip工具  
    - `pip install pyinstaller`  

    ## PyInstaller库使用说明  

    `pyinstaller -F <文件名.py>`  

    - -h 查看帮助  
    - --clean 清理打包过程中的临时文件  
    - -D, --onedir 默认值，生成dist文件夹  
    - -F, --onefile 在dist文件夹中生成独立打包文件  
    - -i <图标.ico> 指定打包程序使用的图标（icon）文件
    """
    )
    return


app._unparsable_cell(
    r"""
    import pyinstaller
    pyinstaller -i curve.ico -F SevenDigitsDrawV2.py
    """,
    name="fact"
)


if __name__ == "__main__":
    app.run()
