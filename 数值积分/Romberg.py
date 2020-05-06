import numpy as np
import matplotlib.pyplot as plt
a=0    # 积分下限
b=1    # 积分上限
eps=1e-6  # 精度
T=[]   # 复化梯形序列
S=[]   # Simpson序列
C=[]   # Cotes序列
R=[]   # Romberg序列
# 被积函数
def f(x):
    if x==0:
        return 1
    else:
        return np.sin(x)/x
# 梯形法
def Tx(a,b,h,t):
    s = 0
    x = a + h / 2
    while x<b:
        s+=f(x)
        x+=h
    return t/2+h*s/2

def romberg(a,b,eps):
    h=b-a
    t=h*(f(a)+f(b))/2
    T.append(t)
    k=1
    while True:
        t=Tx(a,b,h,T[-1])
        T.append(t)
        s=T[-1]+(T[-1]-T[-2])/3
        S.append(s)
        if k>1:
            c = S[-1] + (S[-1] - S[-2]) / 15
            C.append(c)
        if k>2:
            r = C[-1] + (C[-1] - C[-2]) / 63
            R.append(r)
        if k > 3:
            if abs(R[-1] - R[-2]) < eps:
                break
        k += 1
        h = h / 2
    return R[-1]

y=romberg(a,b,eps)
print(y)
print("T[]=",T)
print("S[]=",S)
print("C[]=",C)
print("R[]=",R)


