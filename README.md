# Visualisations
Various Python scripts used to visualise mathematical stuff.

Libraries used:
PyGame - https://pypi.org/project/pygame/
Matplotlib - https://matplotlib.org/
NumPy - https://numpy.org/
perlin-noise - https://pypi.org/project/perlin-noise/

### Map generator
Uses random noise generation to create layers of detail that once combined produces a range of heights resembling natural hills/mountains. The data is then taken and coloured according to the heights and finally a map is made.

Requires perlin-noise, NumPy, Matplotlib

### Map to Line Convertor
Takes height values for a map and plots many 2D line graphs with the y-values determined by a single row of heights on the map. It then displaces them and adds random variation to give a 3D effect.

Requires Matplotlib

### 3DShapeMaker
Takes three lists of coordinates which each describe a polygon. The polygons are placed on a plane made from two of the three standard coordinate axes and extended infinitely on the remaining axis. A large number of points are then tested, and if they are inside of all three of the extended polygons, then they are plotted and shown. The final result is a pseudo 3D-shape. Currently, the program shows a 3D sword.

Requires Matplotlib

![alt text](https://github.com/cazcaz/Visualisations/blob/main/3DSwordVisualisation.gif)

### Fourier
Visualises many circles created by the sines and cosines that make up a fourier series of a function. Since it uses the odd half range expansion for the fourier series, all functions are represented as odd functions when plotted. Pressing the up and down arrow keys changes the accuracy of the visualisation, and the program currently shows the function x^2.

Requires PyGame

![alt text](https://github.com/cazcaz/Visualisations/blob/main/FourierVisualisation.gif)

### Fourier_Piecewise
Creates a simple plot of the fourier series of a piecewise function, inputted as a list of points, and assumes there is a line between each point.

Requires Matplotlib

![alt text](https://github.com/cazcaz/Visualisations/blob/main/PiecewisePlotPicture.png)

### GradientMapPlot
A test to use NumPy for the first time. It takes in a function of x and y and creates a gradient map as a top down view of the function. It currently shows the function (-exp(-xy))/(1-exp(-xy)).

Requires Matplotlib, NumPy

![alt text](https://github.com/cazcaz/Visualisations/blob/main/GradientPlotPicture.png)

### ManyPartilceSim
A test on visualising having lots of particles all under a force directed towards the centre of the screen.

Requires Pygame

![alt text](https://github.com/cazcaz/Visualisations/blob/main/ManyParticleSim.gif)
