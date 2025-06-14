import marimo

__generated_with = "0.11.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""执行marimo edit my_notebook.py启动marimo""")
    return


if __name__ == "__main__":
    app.run()
