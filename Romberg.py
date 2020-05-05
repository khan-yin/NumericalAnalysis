import numpy as np
import matplotlib.pyplot as plt
a=0
b=1
c=1e-5
T=[]            # 复化梯形序列
S=[]            # Simpson序列
C=[]            # Cotes序列
R=[]
def f(x):
    if x==0:
        return 1
    return np.sin(x)/x
# def func(x):
#     return np.append(1,np.sin(x[1:])/x[1:])

def Romberg(a,b,eps):
    h=b-a
    T.append(h*(f(a)+f(b))/2)
    k=1
    while True:
        s=0
        x=a+h/2
        s+=f(x)
        x+=h
        if x>=b:
            t=(T[-1]+h*s)/2
            T.append(t)
            break






