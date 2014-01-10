QucsPython
==========


Controlling qucs simulations from Python.



Underlying Idea
---------------

- Special netlist file describes a circuit with parameters.
- Python fills out parameters (via a simple templating mechanism)
- Python triggers simulation of circuit via qucs
- Python analyzes / displays the output


Current Function
----------------

sensitivity.py, rc_ac.net

rc_ac.net defines an R-C lowpass with parameters Rval and Cval (for the resistor and capacirot, respectively). Python processes this special netlist in that the value for the capacitor is fxed, while the value for the resistor is set to a random value (normal distribution with some mean and variance). Qucs is used to simulate the netlist and Python analyzes the corner frequency of the lowpass.

After several hundred runs, the histogram of the corner frequency is plotted.




Ideas
-----

Use an optimization framework to find "optimal" values for the components of a circuit. In the R-C lowpass, we could try to find a value for the resistor, so that the corner frequency is 4kHz (given a fixed capacitor value).


