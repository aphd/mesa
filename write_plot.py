import sys
import os

def get_fixed_model():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixed-incentives-model')))
    from population_model import PopulationModel
    model = PopulationModel(10, 10, 50, 365)
    return model

def get_variable_model():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'variable-incentives-model')))
    from population_model import PopulationModel
    model = PopulationModel(10, 10, 50, 365)
    return model

def compare_models():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'plot')))
    import plot
    fixed_model = get_fixed_model()
    variable_model = get_variable_model()
    models = [fixed_model, variable_model]
    #plot.run_all(get_fixed_model())
    plot.run_all(models)

def subplot_visualizer():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'plot')))
    from plot.subplot_visualizer import subplot_visualizer
    subplot_visualizer(get_fixed_model())

if __name__ == "__main__":
    subplot_visualizer()

