from population_model import PopulationModel
import matplotlib.pyplot as plt
import numpy as np

# Create the model
model = PopulationModel(10, 10, 50)

# Store additional data
agent_energies = []
good_agents_count = []
bad_agents_count = []

# Run the simulation for 365 steps (days)
for i in range(365):
    model.step()
    
    # Collect data for additional plots
    model_data = model.datacollector.get_model_vars_dataframe()
    
    # Get the average energy of agents
    average_energy = np.mean([agent.energy for agent in model.schedule.agents])
    agent_energies.append(average_energy)
    
    # Count agents by behavior
    good_count = sum(1 for agent in model.schedule.agents if agent.behavior == "good")
    bad_count = sum(1 for agent in model.schedule.agents if agent.behavior == "bad")
    good_agents_count.append(good_count)
    bad_agents_count.append(bad_count)

# Plot 1: Environmental health over time
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(model_data["Environment Health"], label="Environmental Health")
plt.xlabel('Steps (Days)')
plt.ylabel('Environment Health')
plt.title('Environmental Health Over 365 Days')
plt.legend()

# Plot 2: Average Agent Energy over time
plt.subplot(2, 2, 2)
plt.plot(range(365), agent_energies, label="Average Agent Energy", color='orange')
plt.xlabel('Steps (Days)')
plt.ylabel('Average Energy')
plt.title('Average Agent Energy Over Time')
plt.legend()

# Plot 3: Count of Good and Bad Agents over time
plt.subplot(2, 2, 3)
plt.plot(range(365), good_agents_count, label="Good Agents", color='green')
plt.plot(range(365), bad_agents_count, label="Bad Agents", color='red')
plt.xlabel('Steps (Days)')
plt.ylabel('Number of Agents')
plt.title('Count of Agents by Behavior Over Time')
plt.legend()

# Plot 4: Scatter plot of Average Energy vs. Environmental Health
plt.subplot(2, 2, 4)
plt.scatter(agent_energies, model_data["Environment Health"], label="Energy vs. Environment Health", color='purple')
plt.xlabel('Average Agent Energy')
plt.ylabel('Environment Health')
plt.title('Average Energy vs. Environmental Health')
plt.legend()

# Show all plots
plt.tight_layout()
plt.show()
