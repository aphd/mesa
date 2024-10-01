import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from plot_average_energy import plot_average_energy
# from plot_environment_health import plot_environment_health
from write_agent_behavior import write_agent_behavior
# from plot_energy_vs_health import plot_energy_vs_health
# from population_model import PopulationModel

def run_all(model):
    write_agent_behavior(model)
    # plt.subplot(2, 2, 2)
    # plot_average_energy(plt, model)
    # plt.subplot(2, 2, 3)
    # plot_environment_health(plt, model)
    # plt.subplot(2, 2, 4)
    # plot_energy_vs_health(plt, model)
    # plt.tight_layout()
    # plt.show()
    
