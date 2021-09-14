import matplotlib.pyplot as plt
import math
import random
import numpy as np
from MapGen import MapGen

class MoundPlot():

    def __init__(self, height_vals):
        '''
        height_map: index 0,0 corresponds to coordinate 0,0 on the x-y plane (NumPy array !!!!)
        '''
        self.height_map = height_vals
        print("Initialised.")

    def show_plot(self, spacing = 0.1, variance = 0.1, stretch = 1) -> object:
        row_length = len(self.height_map[0])
        col_length = len(self.height_map)
        xvals = np.linspace(0, stretch*row_length, row_length)
        random_offset = np.array([variance*(2*random.random() -1) for _ in range(row_length)])
        set_offset = np.array([spacing for _ in range(row_length)])
        for i in range(col_length):
            plt.plot(xvals, self.height_map[i] + random_offset + i*set_offset, 'k')
        plt.axis('equal')
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    heights = MapGen(256)
    heights.generate_heights(4)
    #heights.falloff()
    mound = MoundPlot(256*heights.access_map())
    mound.show_plot(20, 0, 20)
    heights.generate_image()
