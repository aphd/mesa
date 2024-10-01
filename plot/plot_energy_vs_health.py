import numpy as np

def plot_energy_vs_health(plt, model):
    agent_energies = []
    environment_health_data = []
    duration = model.get_duration()

    for _ in range(duration):
        model.step()
        average_energy = np.mean([agent.energy for agent in model.schedule.agents])
        agent_energies.append(average_energy)
        model_data = model.datacollector.get_model_vars_dataframe()
        environment_health_data.append(model_data["Environment Health"].values[-1])  # Get latest health

    plt.scatter(agent_energies, environment_health_data, label="Energy vs. Environment Health", color='purple')
    plt.xlabel('Average Agent Energy')
    plt.ylabel('Environment Health')
    plt.title('Average Energy vs. Environmental Health')
    plt.legend()


if __name__ == "__main__":
    plot_energy_vs_health()