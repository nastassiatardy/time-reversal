import numpy as np
import os
import matplotlib.pyplot as plt
import imageio
import random as rd
import matplotlib.colors as mcolors

from numerical_values import *


class Antenna:
    def __init__(self, position, report=None):
        self.position = position
        if report is None:
            self.series = []
        elif report is not None:
            self.series = report
    def listen(self, tab):
        t = tab[self.position[0], self.position[1]]
        self.series.append(t)
        return t


class Emission():
    def __init__(self, nb_antennas, positions_antennas=None, size_of_matrix=MATRIX_SIZE, low_val=1, high_val=100):
        self.tab = np.ones((size_of_matrix, size_of_matrix))*low_val
        self.nb_antennas = nb_antennas

        cl, ch = size_of_matrix//2-2, size_of_matrix//2+2
        self.tab[cl:ch, cl:ch] = high_val

        if positions_antennas is None:
            positions_antennas = self.get_positions_antennas(nb_antennas, size_of_matrix)

        self.antennas = {
            f"A_{i}": Antenna(positions_antennas[i]) for i in range(nb_antennas)
        }

        self.positions_antennas = positions_antennas

    def get_positions_antennas(self, nb_antennas, size_of_matrix):
        low = 10
        up = size_of_matrix-10
        l = np.arange(low, up, 10)

        possible_positions = [[low, it] for it in l]
        possible_positions += [[up, it] for it in l]
        possible_positions += [[it, low] for it in l]
        possible_positions += [[it, up] for it in l]

        return rd.sample(possible_positions, k=nb_antennas)

    def transition(self, M1, M2, c=C, Delta_t=DELTA_T, Delta_x=DELTA_X, Delta_y=DELTA_Y, size_of_matrix=MATRIX_SIZE, low_val=1):
        M = np.zeros((size_of_matrix, size_of_matrix))
        gammax = (c*Delta_t/Delta_x)**2
        gammay = (c*Delta_t/Delta_y)**2

        for i in range(1, size_of_matrix-1):
            for j in range(1, size_of_matrix-1):
                M[i,j] = 2*M2[i,j] - M1[i,j] + gammax*(M2[i-1,j] + M2[i+1,j] - 2*M2[i,j]) + gammay*(M2[i,j-1] + M2[i,j+1] - 2*M2[i,j])
        
        report = [antenna.listen(M) for antenna in self.antennas.values()]
        
        return M, report

    def simulate(self, render=False):
        if render:
            if not os.path.exists("emission/"):
                os.makedirs("emission/")

        M1, M2 = self.tab, self.tab
        Nt = int(1/DELTA_T)

        sim_report = {k: [] for k in self.antennas.keys()}
        for i in range(10*Nt):
            T, report = self.transition(M1, M2)
            for ix, aid in enumerate(self.antennas.keys()):
                sim_report[aid].append(report[ix])

            if render:
                cmap = 'viridis'
                norm = mcolors.Normalize(vmin=-100, vmax=100)
                
                plt.close('all')
                plt.imshow(T, cmap=cmap, norm=norm)
                plt.colorbar()
                plt.savefig(f"emission/{i}.png")

            M1, M2 = M2, T
        
        if render:
            frames = [f"emission/{it}.png" for it in range(10*Nt)]
            frames_im = [imageio.imread(fram) for fram in frames]
            imageio.mimsave("emission.gif", frames_im, duration=20)

            for f in os.listdir("emission/"):
                os.remove(f"emission/{f}")
            os.rmdir("emission/")
    
        return sim_report, self.positions_antennas
