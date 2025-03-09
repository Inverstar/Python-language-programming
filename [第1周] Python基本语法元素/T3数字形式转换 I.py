#数字形式转换 I
#初始化一个中文数字字典列表，用于中文数字与阿拉伯数字的转换
arabic_to_chinese = {
    0: '零',
    1: '一',
    2: '二',
    3: '三',
    4: '四',
    5: '五',
    6: '六',
    7: '七',
    8: '八',
    9: '九'
}
str = input()
for i in str:
    print(arabic_to_chinese[int(i)], end='')

template = "零一二三四五六七八九"

s = input()
for c in s:
    print(template[eval(c)], end="")


