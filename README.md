# Simulation of time reversal applied to an electromagnetic wave

### Introduction 

This project implements the refocusing of an electromagnetic wave. In a first stage (`acquisition`) the wave is emitted at the center of the map, and registered using a varying number of antennas. The signals saved by the antennas are then reversed temporally, and re-emitted by the antennas in the map. At the end, we are able to refocus the original wave at the center of the map (`focus` step).


### Propagation of an electromagnetic wave
This work uses a basic 2D equation for propagation of electromagnetic waves, implemented in the `transition` function of the class `Emission` and `Focus`. For a wave $`u`$:

$`
\frac{\partial ^2 u}{\partial t^2} - c^2 \Delta u = s(x,y,t)
`$ (E)

with $`\Delta u = \frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}`$ the laplacian of $`u`$, $`c`$ the speed of the wave in this medium, $`s`$ the source. 

We translate this partial differential equation into a recurrence relation on $`u`$ by using the following result (a classical relation used for the finite difference method): 
$`\frac{\partial^2 f}{\partial x^2}(x,t) ~ \frac{1}{\delta_x^2}(f_{i+1, j} + f_{i-1, j} - 2f_{i,j})`$

with the notation $`f_{i,j} = f(x_i, t_j)`$. 

We get the following update equation on $`u`$:

$`
u_{i,j}^{k+1} = 2u_{i,j}^{k} - u_{i,j}^{k-1} + \gamma_x(u_{i-1,j}^k + u_{i+1,j}^k - 2 u{i,j}^k) + \gamma_y (u_{i,j-1}^k + u_{i,j+1}^k - 2u_{i,j}^k)
`$
with $`\gamma_x = \frac{c^2 \delta_t^2}{\delta_x^2}`$ and $`\gamma_y = \frac{c^2 \delta_t^2}{\delta_y^2}`$ and the analog notation $`u_{i,j}^k = u(x_i, y_j, t_k)`$.

For the limit conditions, we set the border of the map at 0 (limit conditions of Dirichlet).

### Changing parameters

The number of antennas can be modified in the `Emission` class, positions are automatically computed.



### Results

The results are stored in .gif files for visualization, below are displayed an emission example and the corresponding focus:

![alt text](emission. gif) / ! [](emission. gif)

![alt text](focalisation. gif) / ! [](focus. gif)

In the `focus.gif` file we can see the refocus happenning at 1000 steps, which is logical as the antennas store signal for 1000 steps (this can be changed by changing the `DELTA_T` value; the number of steps is equal to $`10 \times \frac{1}{\text{DELTA_T}}`$).
We look at the influence of adding antennas on the quality of refocus:

![alt text](https://github.com/nastassiatardy/time-reversal/main/mean_std.png?raw=true)

### Bibliography

The original time reversal idea was developped by Mathias Fink in various projects.

This simulation could be applied to telecommunications : the phone emits a pulse, which is captured by the antennas. The antennas can then target the position of the phone, leveraging the shape of the environment to their advantage. 

The idea to apply time reversal to telecommunications was developped in the following PhD thesis, by Geoffroy Lerosey, under the direction of Matthias Fink.

Geoffroy Lerosey. Retournement temporel d’ondes électromagnétiques et application à la télécommunication
en milieux complexes. Physics [physics]. ESPCI ParisTECH, 2006. English. ￿NNT : ￿.
￿pastel-00003585￿

