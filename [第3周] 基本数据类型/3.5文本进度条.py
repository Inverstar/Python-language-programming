# TextProBarV1.py
import time
from math import*

def TextProBarV1(s):
    # 进度条版本1
    # 进度条的长度
    scale = 10
    print("------执行开始------")
    for i in range(scale + 1):
        a = '*' * i
        b = '.' * (scale - i)
        c = (i / scale) * 100
        print("\r{:^3.0f}%[{}->{}]".format(c, a, b), end="", flush=True) # \r表示回到行首,flush=True表示强制刷新输出
        time.sleep(s)
    print("\n------执行结束------")
# TextProBarV1(0.1)

#TextProBarV2．py
def TextProBarV2(s):
    for i in range(101): 
        print("\r{:3}%".format(i), end="", flush=True)
        time.sleep(s)

# TextProBarV2(0.01)

#TextProBarV3．py
import time

def f(x, type):
    match type:
        case "Linear":
            Constant = x
            return Constant
        case "Early Pause":
            SpeedsUp = x+(1-sin(2*pi*x+pi/2))/-8
            return SpeedsUp
        case "Late Pause":
            SlowsDown = x+(1-sin(2*pi*x+pi/2))/8
            return SlowsDown
        case "Slow Wavy":
            Constant = x+sin(5*pi*x)/20
            return Constant
        case "Fast Wavy":
            Constant = x+sin(20*pi*x)/80
            return Constant
        case "Power":
            SpeedsUp = (x+(1-x)**0.03)**2
            return SpeedsUp
        case "Inverse Power":
            SlowsDown = 1-(1-x)**1.5
            return SlowsDown
        case "Fast Power":
            SpeedsUp = (x+(1-x)/2)**8
            return SpeedsUp
        case "Inverse Fast Power":
            SlowsDown = 1-(1-x)**3
            return SlowsDown
        
def TextProBarV3(s, type):
    scale = 100
    print("执行开始".center(scale // 2, "-"))
    start = time.perf_counter()
    for i in range(scale + 1):
        k = f(i*0.01, type)
        k = round(k*100)
        a = '*' * k
        b = '.' * (scale - k)
        c = (k / scale) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="", flush=True)
        time.sleep(s)
    print("\n" + "执行结束".center(scale // 2, "-"))

TextProBarV3(0.05,"Early Pause")

