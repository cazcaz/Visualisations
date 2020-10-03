# Visualisations
Various Python scripts used to visualise mathematical stuff.

Libraries used:
PyGame - https://pypi.org/project/pygame/
Matplotlib - https://matplotlib.org/
NumPy - https://numpy.org/

### 3DShapeMaker
Takes three lists of coordinates which each describe a polygon. The polygons are placed on a plane made from two of the three standard coordinate axes and extended infinitely on the remaining axis. A large number of points are then tested, and if they are inside of all three of the extended polygons, then they are plotted and shown. The final result is a psuedo 3D-shape. Currently the program shows a 3D sword.

Requires Matplotlib

### Fourier
Visualises many circles created by the sines and cosines that make up a fourier series of a function. Since it uses the odd half range expansion for the fourier series, all functions are represented as odd functions when plotted. Pressing the up and down arrow keys changes the accuracy of the visualisation, and the program currently shows the function x^2.

Requires PyGame

### Fourier_Piecewise
Creates a simple plot of the fourier series of a piecewise function, inputted as a list of points, and assumes there is a line between each point.

Requires Matplotlib

### GradientMapPlot
A test to use NumPy for the first time. It takes in a function of x and y and creates a gradient map as a top down view of the function. It currently shows the function (-exp(-xy))/(1-exp(-xy)).

Requires Matplotlib, NumPy

### ManyPartilceSim
A test on visualising having lots of particles all under a force directed towards the centre of the screen.

Requires Pygame
