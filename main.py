from acquisition import Emission
from focus import Focus


if __name__ == "__main__":
    emission = Emission(nb_antennas=4)
    sim_report, positions_antennas = emission.simulate() #render=True)
    print(len(sim_report))
    print(len(sim_report["A_1"]))
    # focus = Focus(sim_report, positions_antennas)
    # focus.simulate(render=True)
