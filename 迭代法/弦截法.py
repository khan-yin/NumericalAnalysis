import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*np.exp(x)-1

x=[0.5,0.6]#初始值
y=f(x)
c=1e-6
# print(y)
def xian(x,y,c):
    dy=np.diff(y)
    dx=np.diff(x)
    while(abs(x[-1]-x[-2])>=c):
        m=x[-1]-y[-1]*dx[-1]/dy[-1]
        x.append(m)
        y=f(x)
    return x,y

x,y=xian(x,y,c)
print(x)
print(x[-1])
a=np.linspace(0.5,0.7,1000,endpoint=True)
b=f(a)
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False
plt.title('弦截法')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,'s',label="original values")#蓝点表示原来的值
plt.plot(a,b,'r',label='interpolation values')#曲线
plt.legend(loc=4)
plt.show()