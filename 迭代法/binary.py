import numpy as np
import matplotlib.pyplot as plt

a = 1#左区间
b = 1.5#右区间
c = 0.005#精度

#方程
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

#画图检验
a=np.linspace(1,1.5,100,endpoint=True)
b=func(a)
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False
# plt.rcParams['figure.figsize'] = (8.0, 6.0) # 设置figure_size尺寸
plt.title('二分法')
plt.xlabel('x')
plt.ylabel('y')
plt.text(x, y, (x,y),ha='left', va='top', fontsize=13)
plt.axvline(x=x,ls=":",c="blue")#添加垂直直线
plt.axhline(y=y,ls=":",c="blue")#添加水平直线
plt.plot(x,y,'s',label="original values")#蓝点表示原来的值
plt.plot(a,b,'r',label='interpolation values')#曲线
plt.legend(loc=4)
plt.show()

