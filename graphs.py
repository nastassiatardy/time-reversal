from acquisition import Emission
from focus import Focus

import numpy as np
import os
import matplotlib.pyplot as plt


def generate_focus_fig(nb_antennas_list):
    for nb_antennas in nb_antennas_list:
        emission = Emission(nb_antennas=nb_antennas)
        sim_report, positions_antennas = emission.simulate()
        focus = Focus(sim_report, positions_antennas)
        focus.simulate(render_focus_fig=True)

def fig_analysis(path):
    im_0_antennas = plt.imread(path + "/0antennas.png")
    mean_0, std_0 = np.mean(im_0_antennas), np.std(im_0_antennas)

    antennas_list, means, stds = [], [], []
    list_figs = os.listdir(path)
    list_figs.sort(key=lambda it : int(it.split('antennas')[0]))
    for fig in list_figs:
        fig_path = os.getcwd() + '/' + path + "/" + fig
        im = plt.imread(fig_path)
        antennas_list.append(int(fig.split('antennas')[0]))
        means.append(np.mean(im))
        stds.append(np.std(im))
    
    fig, ax = plt.subplots(1, 2, figsize=(24, 7))
    ax[0].plot(antennas_list, means)
    ax[0].scatter(antennas_list, means, s=10)
    ax[0].set_xlabel("Nb antennas", fontsize=15)
    ax[0].set_ylabel("Mean value of refocus image", fontsize=15)
    ax[0].grid()

    ax[1].plot(antennas_list, stds)
    ax[1].scatter(antennas_list, stds, s=10)
    ax[1].set_xlabel("Nb antennas", fontsize=15)
    ax[1].set_ylabel("Std value of refocus image", fontsize=15)
    ax[1].grid()

    fig.suptitle("Influence of the number of antennas on the refocus", fontsize=30)
    plt.tight_layout()
    plt.savefig(f"mean_std.png")

if __name__ == "__main__":
    # generate_focus_fig(np.arange(0, 21, 1))
    fig_analysis("focus_antennas")


