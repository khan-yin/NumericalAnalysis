x0=0
y0=1
h=0.2
N=6

def func(x,y):
    return y-2*x/y

def rungekutta(x0,y0,h,N):
    n = 1
    while n<N:
        x1=x0+h
        k1=func(x0,y0)
        k2=func(x0+h/2,y0+h*k1/2)
        k3=func(x0+h/2,y0+h*k2/2)
        k4=func(x1,y0+h*k3)
        y1=y0+h*(k1+2*k2+2*k3+k4)/6
        x0=x1
        y0=y1
        n+=1
    return x0,y0

x,y=rungekutta(x0,y0,h,N)
print(x,y)


