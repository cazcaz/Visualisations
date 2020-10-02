from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt 
import numpy as np
from math import pi
import random


#Functions to test if points lie in a polygon

def leftofline(p,l):
    #p is a point
    #l is a pair of coordinates which create a line between them
    if p[0] < l[0][0] and p[0] < l[1][0]:
        return True
    elif p[0] > l[0][0] and p[0] > l[1][0]:
        return False
    else:
        if l[0][1] == l[1][1]:
            return False
        m=(l[0][1]-l[1][1])/(l[0][0]-l[1][0])
        y=m*p[0]-m*l[0][0]+l[0][1]
        if m>0:
            if y >= p[1]:
                return False
            else:
                return True
        else:
            if y <= p[1]:
                return False
            else:
                return True

def inpoly(p,s):
    #p is point
    #s is shape
    temp = 0
    ys=[]
    for j in range(1,len(s)):
        if leftofline(p,[s[j-1],s[j]]):
            ys.append([s[j-1][1],s[j][1]])
    if leftofline(p, [s[len(s)-1],s[0]]):
        ys.append([s[len(s)-1][1],s[0][1]])
    for i in ys:
        e = 1e-10
        m= abs(i[0]+i[1]+2*e)/2
        if abs(p[1]-m) <= abs(i[0]+e-m):
            temp += 1
    if temp %2 == 0:
        return False
    else:
        return True
        
#Define the shapes that will be projected to create the shape (as lists of lists)

xshape=[[3.8,0.3],[4.5,0.3],[4.5,2.3],[6,2.3],[6,2.5],[5,2.5],[5,8.5],[3.4,9.8],[3.4,2.5],[2.3,2.5],[2.3,2.3],[3.8,2.3]]
yshape=[[3.8,0.3],[4.5,0.3],[4.5,2.3],[4.7,2.3],[4.7,2.5],[4.4,2.5],[4.4,8.5],[4.2,9.8],[4.1,9.8],[3.9,8.5],[3.9,2.5],[3.6,2.5],[3.6,2.3],[3.8,2.3]]
zshape=[[2.3,4.7],[6.1,4.7],[6.1,3.85],[2.3,3.85]]

#Test a multitude of points and whether they lie in the 3 shapes
#Keep the amount of decimal points of the points to be less than 9

#The ranges of values that can be tested by random points
rangex=[2.2,6.2]
rangey=[3.4,4.8]
rangez=[0,10]

PointAmount=100000
FinalPoints=[]
for i in range(1,PointAmount+1):
    x=[random.uniform(rangex[0],rangex[1]),random.uniform(rangey[0],rangey[1]),random.uniform(rangez[0],rangez[1])]
    if inpoly([x[0],x[2]],xshape):
        if inpoly([x[1],x[2]],yshape):
            if inpoly([x[0],x[1]],zshape):
                FinalPoints.append(x)

#Turn Finalpoints into lists of xs, ys and zs
xdata=[]
ydata=[]
zdata=[]
for i in FinalPoints:
    xdata.append(i[0])
    ydata.append(i[1])
    zdata.append(i[2])


#Plot the points

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
ax.scatter3D([0,0,0,0,10,10,10,10], [0,0,10,10,0,0,10,10], [0,10,0,10,0,10,0,10])
plt.show()