from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt
x=[100,121,144]
y=[10,11,12]
data_x=np.array(x)
data_y=np.array(y)
def pxlagrange(x,y):
    l=len(x)
    p = np.poly1d(0.0)
    for k in range(l):
        s=y[k]
        for j in range(l):
            if j==k:
                continue
            fac=x[k]-x[j]
            s*=np.poly1d([1.0,-x[j]])/fac
        p+=s
    return p
a=pxlagrange(x,y)
print("p(x)=\n",a)
print("p(115)=",a(115))

