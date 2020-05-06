import numpy as np
import matplotlib.pyplot as plt
a=0#积分下限
b=1#积分上限
c=1e-4#精确度
# 被积函数
def func(x):
    return np.append(1,np.sin(x[1:])/x[1:])

t1=(1-0)/1*(1+np.sin(1)/1)/2
# print(t1)
n = 2
while True:
    h = (b - a) / n
    arr = np.linspace(a, b, n + 1, endpoint=True)
    y = func(arr)
    t = h * (2 * sum(y) - y[0] - y[-1]) / 2
    # print(t)
    n = n + 1
    # print("t1=",t1)
    # print("t=",t)
    print(abs(t-t1))
    if abs(t-t1)<c:
        t1=t
        break
    else:
        t1=t

print("t={},n={}".format(t1,n))

