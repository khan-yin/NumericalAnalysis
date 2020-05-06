import numpy as np
import matplotlib.pyplot as plt
from sympy import diff, symbols
from sympy import exp
x0=10.0
def func(x0):
    x = symbols('x', real=True)
    #y=x*exp(x)-1
    y=x**2-115
    v=x-y/diff(y,x,1)#diff部分是对f(x)求1阶导数。整个式子就是牛顿法的迭代式子
    # print(v)输出迭代的公式
    return v.subs(x,x0)

def newton(x0):
    while True:
        x=func(x0)
        print(x)
        if abs(x-x0)<1e-6:
            break
        else:
            x0 = x
    return x

print("√115=",newton(x0))
