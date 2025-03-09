Money = input()
if "RMB" in Money:
    C = eval(Money[3:])/6.78
    print("USD{:.2f}".format(C))
elif "USD" in Money:
    F = eval(Money[3:])*6.78
    print("RMB{:.2f}".format(F))
else:
    print("输入格式错误")

CurStr = input()
if CurStr[:3] == "RMB":
    print("USD{:.2f}".format(eval(CurStr[3:])/6.78))
elif CurStr[:3] in ['USD']:
    print("RMB{:.2f}".format(eval(CurStr[3:])*6.78))