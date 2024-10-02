import sys
import os

def get_fixed_model():
    sys.path.insert(0, variable_path) if (variable_path := os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixed-incentives-model'))) not in sys.path else None
    import fixed_population_model
    model = fixed_population_model.PopulationModel(10, 10, 50, 350)
    return model

def get_variable_model():
    sys.path.insert(0, variable_path) if (variable_path := os.path.abspath(os.path.join(os.path.dirname(__file__), 'variable-incentives-model'))) not in sys.path else None
    import variable_population_model
    model = variable_population_model.PopulationModel(10, 10, 50, 350)
    return model

def compare_models():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'plot')))
    from plot.compare_models import compare_models
    compare_models([get_fixed_model(), get_variable_model()])

def subplot_visualizer():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'plot')))
    from plot.subplot_visualizer import subplot_visualizer
    subplot_visualizer(get_fixed_model())

if __name__ == "__main__":
    compare_models()
    # subplot_visualizer()
