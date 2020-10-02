import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from math import exp

autumn = cm.get_cmap('autumn',256)

def fc(x,y):
    x1=np.multiply(x,-y)
    x2=np.power(exp(1),x1)
    x3=np.multiply(x2,-1)
    x4=np.subtract(1,x2)
    return np.divide(x3,x4)


defined=0.1

x= np.linspace(-defined,defined,50)
y= np.linspace(-defined,defined,50)

X, Y = np.meshgrid(x,y)

f=fc(X,Y)
fig,ax=plt.subplots(1,1)

levels=np.linspace(f.min(),f.max(),20)

ax.set_title('Plot')
norm = cm.colors.Normalize(vmax=f.max(), vmin=f.min())
cp = ax.contourf(X,Y,f,levels, norm=norm)
cp.set_cmap(autumn)


fig.colorbar(cp)

plt.show()