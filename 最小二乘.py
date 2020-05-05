import numpy as np
import matplotlib.pyplot as plt
x=np.array([165,123,150,123,141])
xm=x
y=np.array([187,126,172,125,148])
l=len(x)
x.reshape(l,1)
y.reshape(l,1)
b=np.ones((l,1))
x=np.c_[x,b]
# print(x)
w=np.linalg.inv(x.T@x)@x.T@y#最小二乘矩阵形式
# w= np.dot(np.dot(np.linalg.inv(np.dot(x.T, x)), x.T), y)
print(w)
print(xm[0]*w[0]+w[1])
#画图检验
xs=np.linspace(np.min(xm),np.max(xm),10,endpoint=True)
ys=xs*w[0]+w[1]#拟合函数y的预测值计算
plt.plot(xm,y,'s',label="original values")#蓝点表示原来的值
plt.plot(xs,ys,'r',label='interpolation values')#插值曲线
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)#指定legend的位置右下角
plt.show()