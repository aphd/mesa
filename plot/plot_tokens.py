# plot/plot_tokens.py
def plot_tokens(plt, model):
    total_days = model.get_duration()
    token_data = []

    # Run the simulation for the specified number of steps (days)
    for _ in range(total_days):
        model.step()

        # Collect tokens for all agents
        total_tokens = sum(agent.token for agent in model.schedule.agents)
        token_data.append(total_tokens)

    # Create a plot with days on the x-axis and accumulated tokens on the y-axis
    plt.plot(range(total_days), token_data, label='Total Tokens')

    set_xlabel = plt.set_xlabel if hasattr(plt, 'set_xlabel') else plt.xlabel
    set_ylabel = plt.set_ylabel if hasattr(plt, 'set_ylabel') else plt.ylabel
    set_title = plt.set_title if hasattr(plt, 'set_title') else plt.title
    set_xlabel('Days')
    set_ylabel('Accumulated Tokens')
    set_title('Tokens Accumulated by Agents Over Time')

    plt.grid(True)
    plt.legend()

# Example usage
if __name__ == "__main__":
    pass