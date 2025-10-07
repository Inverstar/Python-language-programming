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
        """
    # 基本统计值计算

    ## 总个数

    ## 求和

    ## 平均值

    ## 方差

    ## 中位数
    """
    )
    return


if __name__ == "__main__":
    app.run()
