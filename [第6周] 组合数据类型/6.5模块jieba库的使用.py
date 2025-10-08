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
    # 模块5:jieba库的使用

    ## jieba库是优秀的中文分词第三方库

    - 中文文本需要通过分词获得单个的词语
    - jieba是优秀的中文分词第三方库，需要额外安装
    - jieba库提供三种分词模式，最简单只需掌握一个函数

    ## jieba分词依靠中文词库

    - 利用一个中文词库确定中文字符之间的关联概率
    - 中文字符间概率大的组成词组，形成分词结果
    - 除了分词，用户还可以添加自定义的词组

    ## jieba分词三种模式

    - 精确模式：把文本精确的切分开，不存在冗余单词  
    - 全模式：把文本中所有可能的词语都扫描出来，有余  
    - 搜索引擎模式：在精确模式基础上，对长词再次切分
    """
    )
    return


@app.cell
def _():
    import jieba
    #精确模式
    jieba.lcut("中国是一个伟大的国家")
    #全模式
    jieba.lcut("中国是一个伟大的国家",cut_all=True)
    #搜索引擎模式
    jieba.lcut_for_search("中华人民共和国是伟大的")
    #分词词典增加新词
    jieba.add_word("蟒蛇语言")
    return


if __name__ == "__main__":
    app.run()
