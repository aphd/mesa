import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from plot_average_energy import plot_average_energy
# from plot_environment_health import plot_environment_health
# from plot_agent_behavior import plot_agent_behavior
# from plot_energy_vs_health import plot_energy_vs_health
from plot.plot_tokens import plot_tokens
import matplotlib.pyplot as plt

def compare_tokens(models):
    # Create a single figure and axis for all plots
    plt.figure(figsize=(12, 8))
    ax = plt.gca()  # Get the current axis
    
    for index, model in enumerate(models):
        print(model.get_name())
        print(f"Index: {index}, Element: {model}")
        plot_tokens(ax, model)
    
    plt.legend([model.get_name() for model in models], loc='upper right')
    plt.tight_layout()
    plt.show()
