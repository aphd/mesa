from population_model import PopulationModel

def plot_agent_behavior(plt):
    model = PopulationModel(10, 10, 50)
    good_agents_count = []
    bad_agents_count = []

    for _ in range(365):
        model.step()
        good_count = sum(1 for agent in model.schedule.agents if agent.behavior == "good")
        bad_count = sum(1 for agent in model.schedule.agents if agent.behavior == "bad")
        good_agents_count.append(good_count)
        bad_agents_count.append(bad_count)

    plt.plot(range(365), good_agents_count, label="Good Agents", color='green')
    plt.plot(range(365), bad_agents_count, label="Bad Agents", color='red')
    plt.xlabel('Days')
    plt.ylabel('Number of Agents')
    plt.title('Count of Agents by Behavior Over 365 Days')
    plt.legend()

if __name__ == "__main__":
    plot_agent_behavior()