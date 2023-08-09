# time-reversal

This project implements the refocalisation of an electromagnetic wave. In a first stage (acquisition) the wave is emitted at the center of the map, and registered using 
a varying number of antennas. The signal saved by the antennas are then reversed temporally, and re-emitted by the antennas in the map. At the end, we are able to
refocalise the original wave at the center of the map (refocalisation step).

This work uses a basic 2D equation for propagation of electromagnetic waves. The original time reversal idea was developped by Mathias Fink in various projects.

This simulation could be applied to telecommunications : the phone emits a pulse, which is captured by the antennas. The antennas can then target the position of the phone,
leveraging the shape of the environment to their advantage. 