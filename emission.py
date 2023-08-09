import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
import matplotlib.colors as mcolors

from numerical_values import *


def get_initial_matrix(size_of_matrix=MATRIX_SIZE, low_val=1, high_val=100, antennas=None):
    M = np.ones((size_of_matrix, size_of_matrix))*low_val
    center = size_of_matrix//2
    for i in range(center - 2, center + 2):
        for j in range(center - 2, center + 2):
            M[i,j] = high_val
    if antennas is not None:
        for a in antennas.values():
            M[a.position[0], a.position[1]] = a.series[-1]
    return M
