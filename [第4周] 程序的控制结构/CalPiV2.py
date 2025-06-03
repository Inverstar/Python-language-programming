#CalPiV2.py
from random import random
from time import perf_counter
# 使用蒙特卡洛方法计算圆周率

def monte_carlo_PI(X=1):
    X = 10**X
    DARTS = X * X
    hits = 0.0
    start = perf_counter()
    for i in range(1, DARTS + 1):
        x, y = random(), random()
        dist = pow(x ** 2 + y ** 2, 0.5)
        if dist <= 1.0:
            hits = hits + 1
    pi = 4 * (hits / DARTS)
    print("圆周率值是: {}".format(pi))
    print("运行时间是: {:.5f}s".format(perf_counter() - start))

monte_carlo_PI(1)
monte_carlo_PI(2)
monte_carlo_PI(3)
monte_carlo_PI(4)