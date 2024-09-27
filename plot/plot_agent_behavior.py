def plot_agent_behavior(plt, model):
    good_agents_count = []
    bad_agents_count = []
    duration = model.get_duration()
    for _ in range(duration):
        model.step()
        good_count = sum(1 for agent in model.schedule.agents if agent.behavior == "good")
        bad_count = sum(1 for agent in model.schedule.agents if agent.behavior == "bad")
        good_agents_count.append(good_count)
        bad_agents_count.append(bad_count)

    plt.plot(range(duration), good_agents_count, label="Good Agents", color='green')
    plt.plot(range(duration), bad_agents_count, label="Bad Agents", color='red')
    plt.xlabel('Days')
    plt.ylabel('Number of Agents')
    plt.title(f'Count of Agents by Behavior Over {duration} Days')
    plt.legend()

if __name__ == "__main__":
    plot_agent_behavior()