#CalPiV1.py
from time import perf_counter
# 使用莱布尼兹公式计算圆周率
def leibniz_pi(N=100):
    pi = 0
    start = perf_counter()
    for k in range(N):
        pi += 1/pow(16,k)*( 
                  4/(8*k+1) - 2/(8*k+4) - 
                  1/(8*k+5) - 1/(8*k+6) ) 
    print("圆周率值是: {}".format(pi))
    print("运行时间是: {:.5f}s".format(perf_counter() - start))

leibniz_pi(N=10)
leibniz_pi()
leibniz_pi(N=1000)
leibniz_pi(N=10000)