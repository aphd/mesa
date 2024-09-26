from model import PopulationModel
import matplotlib.pyplot as plt

# Create the model
model = PopulationModel(10, 10, 50)

# Run the simulation for 100 steps
for i in range(100):
    model.step()

# Plot the environmental health
model_data = model.datacollector.get_model_vars_dataframe()
plt.plot(model_data["Environment Health"], label="Environmental Health")
plt.legend()
plt.show()
