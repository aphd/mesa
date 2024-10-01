import numpy as np

def plot_average_energy(plt, model):
    agent_energies = []
    duration = model.get_duration()

    for _ in range(duration):
        model.step()
        average_energy = np.mean([agent.energy for agent in model.schedule.agents])
        agent_energies.append(average_energy)

    plt.plot(range(duration), agent_energies, label="Average Agent Energy", color='orange')
    plt.xlabel('Days')
    plt.ylabel('Average Energy')
    plt.title(f'Average Agent Energy Over {duration} Days')
    plt.legend()

if __name__ == "__main__":
    plot_average_energy()