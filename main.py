from acquisition import Emission
from focalisation import Focalisation


if __name__ == "__main__":
    emission = Emission(nb_antennas=4)
    sim_report, positions_antennas = emission.simulate() # render=True)

    focalisation = Focalisation(sim_report, positions_antennas)
    focalisation.simulate(render=True)
