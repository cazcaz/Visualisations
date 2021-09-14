import numpy as np
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random
import sys
import time
import math


class MapGen:
    def __init__(self, size=256):
        self.N = size
        self.shadows_exist = False
        self.map_exists = False
        colour_vals = self.generate_colours()
        self.height_values = np.zeros((self.N, self.N))
        self.shadow_map = np.zeros((self.N, self.N))
        self.map_colours = ListedColormap(colour_vals)
        print("Colour map generated.")

    def generate_colours(self):
        # Doesn't allow for any customisation, it is just stored in this function to avoid clutter
        colour_list = []
        darkestsea = [0, 26 / 255, 1, 1]
        darkersea = [0, 119 / 255, 1, 1]
        lightsea = [0, 188 / 255, 1, 1]
        sand = [1, 243 / 255, 124 / 255, 1]
        grass = [41 / 255, 151 / 255, 67 / 255, 1]
        rock = [134 / 255, 134 / 255, 134 / 255, 1]
        snow = [245 / 255, 245 / 255, 245 / 255, 1]

        snowpc = 20 / 100
        rockpc = 15 / 100
        grasspc = 10 / 100
        sandpc = 5 / 100
        lightseapc = 5 / 100
        darkerseapc = 15 / 100
        darkestseapc = 30 / 100

        for _ in range(int(darkestseapc * 256)):
            colour_list.append(darkestsea)
        for _ in range(int(darkerseapc * 256)):
            colour_list.append(darkersea)
        for _ in range(int(lightseapc * 256)):
            colour_list.append(lightsea)
        for _ in range(int(sandpc * 256)):
            colour_list.append(sand)
        for _ in range(int(grasspc * 256)):
            colour_list.append(grass)
        for _ in range(int(rockpc * 256)):
            colour_list.append(rock)
        for _ in range(int(snowpc * 256)):
            colour_list.append(snow)
        return colour_list

    def generate_heights(self, detail=1, freqmult=0.5):
        # Creates the random noise used to define the heights on the map
        noisemaps = []
        start_time = time.time()

        print("Generating noise:")
        percentage = 100 // detail

        for i in range(1, detail + 1):
            noisemaps.append(PerlinNoise(2 ** i, random.randint(1, 1000)))

        for k in range(len(noisemaps)):
            self.height_values += freqmult ** k * np.array(
                [[noisemaps[k]([i / self.N, j / self.N]) for j in range(self.N)] for i in range(self.N)])
            print("(" + str(percentage * (k + 1)) + "%" + " " + str(time.time() - start_time) + "s)", end=" ")
            sys.stdout.flush()

        print("Noise generated!")
        self.normalise_map(self.height_values)
        self.map_exists = True

    def falloff(self):
        # Creates a falloff effect so that the height is concentrated in the middle
        falloff_map = np.zeros((self.N, self.N))
        for i in range(self.N):
            for j in range(self.N):
                falloff_map[i][j] = 1 - abs((j - self.N // 2) / self.N - (i - self.N // 2) / self.N) - abs(
                    (j - self.N // 2) / self.N + (i - self.N // 2) / self.N)
        # Using an add here gives an ocean boundary, but using a multiply gives a grass boundary
        self.height_values += falloff_map

    def normalise_map(self, heatmap):
        maxs = []
        mins = []
        for i in heatmap:
            maxs.append(max(i))
            mins.append(min(i))
        totmax = max(maxs)
        totmin = min(mins)
        heatmap -= totmin
        if totmax != totmin:
            heatmap = heatmap / (totmax - totmin)

    def generate_image(self):
        # Outputs the final map image

        # Default values
        w = 10
        h = 10
        d = 70

        tuple_list1 = [tuple(x) for x in self.height_values]
        tuple_list2 = [tuple(y) for y in self.shadow_map]
        plt.figure(figsize=(w, h), dpi=d)
        if self.map_exists == False:
            print("No map generated!")
        else:
            if self.map_exists == True:
                plt.imshow(tuple_list1, self.map_colours)
            if self.shadows_exist == True:
                plt.imshow(tuple_list2, self.shadows_cmap)

        plt.axis('off')
        plt.show()

    def shade_compute(self, h1, h2, i1, i2, angle):
        # Tests all values in the same column from the correct direction to decide whether a pixel will be shaded

        # Not currently finished!
        h_diff = 500 * (h2 - h1)
        i_diff = np.abs(i2 - i1)
        opp = h_diff * math.tan(math.pi / 2 - angle)
        final_temp = opp - i_diff
        final = np.zeros(self.N)
        for i in range(self.N):
            if final_temp[i] <= 0:
                final[i] = 0
            else:
                final[i] = 1
        return final

    def shade_map(self, direction="N", angle=math.pi / 4):
        # Generates a shade map through the use of many different opacities of black layered on top of one another

        # Not currently finished!
        shadows_temp = np.zeros((256, 4))
        opacity_range = np.linspace(0, 0.7, 256)

        for i in range(256):
            shadows_temp[i][3] = opacity_range[i]

        self.shadows_cmap = ListedColormap(shadows_temp)

        dir_dict = {
            "N": -1,
            "E": 1,
            "S": 1,
            "W": -1
        }
        buffered_list = np.zeros((self.N + 2, self.N + 2))

        for i in range(self.N):
            buffered_list[i + 1][1:self.N + 1] = np.copy(self.height_values[i])

        print("Generating shade map:")
        start_time = time.time()

        holding_shadow_map = np.zeros((self.N, self.N))
        for j in range(1, self.N + 1):
            p = 1
            if direction == "E" or direction == "W":
                temp_buffer_map = np.copy(np.transpose(buffered_list))
            else:
                temp_buffer_map = np.copy(buffered_list)
            while j + p * dir_dict[direction] >= 0 and j + p * dir_dict[direction] < self.N:
                start_val = j
                start_vals = np.zeros(self.N)
                for i in range(self.N):
                    start_vals[i] = start_val
                height1 = np.copy(temp_buffer_map[j][1:self.N + 1])
                height2 = np.copy(temp_buffer_map[j + p * dir_dict[direction]][1:self.N + 1])
                holding_shadow_map[j - 1] += self.shade_compute(height1, height2, start_vals, start_vals + p, angle)
                p += 1
        if direction == "E" or direction == "W":
            self.shadow_map = np.copy(np.transpose(holding_shadow_map))
        else:
            self.shadow_map = np.copy(holding_shadow_map)

        self.shadows_exist = True
        print("Shading generated in " + str(time.time() - start_time) + "s!")

    def access_map(self):
        # A getter function for the raw values of the heights in a map
        if self.map_exists:
            return self.height_values


if __name__ == "__main__":
    mapp = MapGen(1024)
    mapp.generate_heights(4, 0.5)
    mapp.falloff()
    mapp.generate_image()
