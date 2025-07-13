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
        # 学习平台
    
        <https://python123.io>
        """
    )
    return


if __name__ == "__main__":
    app.run()
