import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from plot_average_energy import plot_average_energy
from plot_environment_health import plot_environment_health
from plot_agent_behavior import plot_agent_behavior
from plot_energy_vs_health import plot_energy_vs_health

def run_all():

    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    plot_average_energy(plt)
    plt.subplot(2, 2, 2)
    plot_agent_behavior(plt)
    plt.subplot(2, 2, 3)
    plot_environment_health(plt)
    plt.subplot(2, 2, 4)
    plot_energy_vs_health(plt)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_all()
