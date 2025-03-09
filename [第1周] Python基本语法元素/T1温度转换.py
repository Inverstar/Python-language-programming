#TempConvert.py
TempStr = input()
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("{:.2f}F".format(F))
else:
    print("输入格式错误")
#(1) 将输入字符串转换为数字时使用eval()函数，不要用int()函数，因为输入的数字可能不是整数；
#(2) 采用{:.2f}将输出数字变成两位小数点表示时，即使数学上该输出值是整数，也会按照小数方式输出，例如，转换后温度为10度，输出为10.00。