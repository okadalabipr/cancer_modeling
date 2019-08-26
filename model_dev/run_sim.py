"""
This is the file that is used to actually run the simulations for your model and 
plot the results.
"""

from simulation import Simulation
import plot_func

def run_simulation():
    sim = Simulation()

    plot_func.timecourse(sim)


if __name__ == "__main__":
    run_simulation()