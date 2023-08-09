import os
import numpy as np
import imageio
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from emission import get_initial_matrix
from numerical_values import *
from acquisition import Antenna


class Focalisation:
    def __init__(self, sim_report, positions_antennas):
        self.sim_report = sim_report
        self.sim_report_rt = {
            aid: self.sim_report[aid][::-1]
            for aid in self.sim_report.keys()
        }
    
        self.antennas = {
            k: Antenna(positions_antennas[i], self.sim_report_rt[k]) for i, k in enumerate(self.sim_report_rt.keys())
        }

        self.tab = get_initial_matrix(size_of_matrix=MATRIX_SIZE, low_val=1, high_val=1, antennas=self.antennas)

    def transition(self, M1, M2, c=C, Delta_t=DELTA_T, Delta_x=DELTA_X, Delta_y=DELTA_Y, size_of_matrix=MATRIX_SIZE, low_val=1):
        M = np.zeros((size_of_matrix, size_of_matrix))
        gammax = (c*Delta_t/Delta_x)**2
        gammay = (c*Delta_t/Delta_y)**2

        for i in range(1, size_of_matrix-1):
            for j in range(1, size_of_matrix-1):
                M[i,j] = 2*M2[i,j] - M1[i,j] + gammax*(M2[i-1,j] + M2[i+1,j] - 2*M2[i,j]) + gammay*(M2[i,j-1] + M2[i,j+1] - 2*M2[i,j])
        
        return M
    
    def simulate(self, render=False):
        if render:
            if not os.path.exists("focalisation/"):
                os.makedirs("focalisation/")

        M1, M2 = self.tab, self.tab
        Nt = int(1/DELTA_T)

        for i in range(10*Nt + 100):
            T = self.transition(M1, M2)

            if render:
                cmap = 'viridis'
                norm = mcolors.Normalize(vmin=-10, vmax=10)
                
                plt.close('all')
                plt.imshow(T, cmap=cmap, norm=norm)
                plt.colorbar()
                plt.savefig(f"focalisation/{i}.png")

            M1, M2 = M2, T
            if i < 10*Nt:
                for aid, antenna in self.antennas.items():
                    pos = antenna.position
                    M1[pos[0], pos[1]] = self.sim_report_rt[aid][i]
                    M2[pos[0], pos[1]] = self.sim_report_rt[aid][i]
        
        if render:
            frames = [f"focalisation/{it}.png" for it in range(10*Nt + 100)]
            frames_im = [imageio.imread(fram) for fram in frames]
            imageio.mimsave("focalisation.gif", frames_im, duration=20)

            for f in os.listdir("focalisation/"):
                os.remove(f"focalisation/{f}")
            os.rmdir("focalisation/")
    
        return True
