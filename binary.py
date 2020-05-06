import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 1.5
c = 0.005

def func(x):
    return x ** 3 - x - 1
def binary_solve(a,b,c):
    k = 0
    x = (a + b) / 2
    y = func(x)
    while abs(b-a)>=c:
        y0 = func(a)
        x = (a + b) / 2
        y = func(x)
        k += 1
        if y*y0 <= 0:
            b = x
        else:
            a = x
        # print(x)
    return x,y,k

x,y,k=binary_solve(a,b,c)

print("x={},y={},k={}".format(x,y,k))
