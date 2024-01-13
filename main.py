from acquisition import Emission
from focus import Focus


if __name__ == "__main__":
    emission = Emission(nb_antennas=4)
    sim_report, positions_antennas = emission.simulate(render=True)
    focus = Focus(sim_report, positions_antennas)
    focus.simulate(render=True)
