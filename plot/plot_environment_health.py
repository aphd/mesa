from population_model import PopulationModel
import numpy as np

def plot_environment_health(plt):
    model = PopulationModel(10, 10, 50)
    environment_health_data = []

    for _ in range(365):
        model.step()
        model_data = model.datacollector.get_model_vars_dataframe()
        environment_health_data.append(model_data["Environment Health"].values[-1])  # Get latest health

    plt.plot(environment_health_data, label="Environmental Health")
    plt.xlabel('Days')
    plt.ylabel('Environment Health')
    plt.title('Environmental Health Over 365 Days')
    plt.legend()

if __name__ == "__main__":
    plot_environment_health()