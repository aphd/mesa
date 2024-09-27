from population_model import PopulationModel
import numpy as np

def plot_average_energy(plt):
    model = PopulationModel(10, 10, 50)
    agent_energies = []

    for _ in range(365):
        model.step()
        average_energy = np.mean([agent.energy for agent in model.schedule.agents])
        agent_energies.append(average_energy)

    plt.plot(range(365), agent_energies, label="Average Agent Energy", color='orange')
    plt.xlabel('Days')
    plt.ylabel('Average Energy')
    plt.title('Average Agent Energy Over 365 Days')
    plt.legend()

if __name__ == "__main__":
    plot_average_energy()