import numpy as np
import matplotlib.pyplot as plt
x=np.array([-2,-1,0,1,2,3])
y=np.array([-5,1,1,1,7,25])
# x=np.array([100,121,144])
# y=np.array([10,11,12])
def chashang(l):
    p=0
    if(l==0):
        return y[l]
    for k in range(l):
        f=y[k]
        s=1.0
        for j in range(l):
            if j==k:
                continue
            s*=(x[k]-x[j])
        p+=f/s
    return p

def newt(x):
    l = len(x)
    w = np.poly1d(1)
    p=0
    for k in range(l):

        f=chashang(k+1)
        # print("f=",f)
        p+=w*f
        w*=np.poly1d([1.0,-x[k]])
        # print(p)
    return p

New=newt(x)
print(New)
# print(New(115))

#画图检验
xs=np.linspace(np.min(x),np.max(x),1000,endpoint=True)
ys=[]
for i in xs:
    ys.append(New(i))
plt.title("newton_interpolation")
plt.plot(x,y,'s',label="original values")#蓝点表示原来的值
plt.plot(xs,ys,'r',label='interpolation values')#插值曲线
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)#指定legend的位置右下角
plt.show()
