#a1 = 1/2
#am = 0 , m = 1,2,3,...
#bn = 0 if n even
#bn = 2/(n*pi) if n odd

from matplotlib import pyplot as plt 
from math import sin,cos,pi

function_points=[[0,2],[2,2],[3,1],[3.0, -1.0], [3.25, -0.875], [3.5, -0.5], [3.75, 0.125], [4.0, 1.0], [4.25, 2.125], [4.5, 3.5],[7,-1.5],[10,-1.5]]
L=function_points[len(function_points)-1][0]-function_points[0][0]

def def_integral(a,b,f,n):
    accuracyn =100
    xvalues = [a + (b-a)*i/accuracyn for i in range(accuracyn)]
    yvalues = [f(i,n) for i in xvalues]
    rectangles = [yvalues[i]*(b-a)/accuracyn for i in range(len(xvalues))]
    return sum(rectangles)

def f(x,n):
    for i in range(len(function_points)-1):
        if x>= function_points[i][0] and x< function_points[i+1][0]:
            return line(function_points[i],function_points[i+1],x)*sin(n*pi*x/L)
    
def line(p1,p2,x):
    return (p2[1]-p1[1])/(p2[0]-p1[0])* x + p2[1] -(p2[1]-p1[1])/(p2[0]-p1[0])*p2[0]

def coeffs_a(n):
    if n == 0:
        return 0
    else:
        return 0

def coeffs_b(n):
    coeff = def_integral(0,L,f,n)
    return coeff

def fourier(n,x):
    sines = [coeffs_a(i)*cos(i*pi*2*x/L) for i in range(n+1)]
    cosines = [coeffs_b(i)*sin(i*pi*2*x/L) for i in range(1,n+1)]
    return coeffs_a(0) + sum(sines) + sum(cosines)




accuracy= 2000
xlst = [L*i/accuracy for i in range(accuracy +1)]
ylst = [fourier(50,i) for i in xlst]

plt.plot(xlst,ylst,'-')
plt.show()