#TempConvert.py
TempStr = input()
if TempStr[0] in ['F']:
    C = (eval(TempStr[1:]) - 32)/1.8
    print("C{:.2f}".format(C))
elif TempStr[0] in ['C']:
    F = 1.8*eval(TempStr[1:]) + 32
    print("F{:.2f}".format(F))
else:
    print("输入格式错误")
#(1) 将输入字符串转换为数字时使用eval()函数，不要用int()函数，因为输入的数字可能不是整数；

#(2) 采用{:.2f}将输出数字变成两位小数点表示时，即使数学上该输出值是整数，也会按照小数方式输出，例如，转换后温度为10度，输出为10.00；

#(3) TempStr[1:]表示字符串除首字符外的所有字符。