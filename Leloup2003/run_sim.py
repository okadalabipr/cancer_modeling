from model.simulation import Simulation
import plot_func

def run_simulation():
    sim = Simulation()

    plot_func.timecourse(sim)


if __name__ == "__main__":
    run_simulation()