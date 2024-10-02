import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from plot_average_energy import plot_average_energy
from plot_environment_health import plot_environment_health
from plot_agent_behavior import plot_agent_behavior
from plot_energy_vs_health import plot_energy_vs_health
from plot_tokens import plot_tokens

def subplot_visualizer(model):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 2, 1)
    plot_agent_behavior(plt, model)

    plt.subplot(3, 2, 2)
    plot_tokens(plt, model)

    plt.subplot(3, 2, 3)
    plot_average_energy(plt, model)

    plt.subplot(3, 2, 4)
    plot_environment_health(plt, model)

    plt.subplot(3, 2, 5)
    plot_energy_vs_health(plt, model)

    plt.tight_layout()
    plt.show()
    
