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
    # 文本词频统计

    ## 文本资料

    - 英文文本：Hamet分析词频
    https://python123.io/resources/pye/hamlet.txt
    - 中文文本：《三国演义》分析人物
    https://python123.io/resources/pye/threekingdoms.txt
    """
    )
    return


if __name__ == "__main__":
    app.run()
