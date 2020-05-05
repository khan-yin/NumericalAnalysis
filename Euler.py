##改进欧拉法

def func(x,y):
    return y-2*x/y

def prove_euler(x0,y0,h,N):
    n=1
    while(n<N):
        x1=x0+h
        y_p=y0+h*func(x0,y0)
        y_c=y0+h*func(x1,y_p)
        y1=(y_p+y_c)/2
        n+=1
        x0=x1
        y0=y1
    return x1,y1

x0=0
y0=1
h=0.1
N=11
x1,y1=prove_euler(x0,y0,h,N)
print(x1,y1)