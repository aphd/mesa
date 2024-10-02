import sys
import os
import importlib

def get_fixed_model():
    fixed_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixed-incentives-model'))
    if fixed_path not in sys.path:
        sys.path.insert(0, fixed_path)
    
    # Import the module and reload it
    import fixed_population_model
    importlib.reload(fixed_population_model)  # Reload the entire module
    
    # Now access the class from the reloaded module
    model = fixed_population_model.PopulationModel(10, 10, 50, 350)
    return model

def get_variable_model():
    variable_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'variable-incentives-model'))
    if variable_path not in sys.path:
        sys.path.insert(0, variable_path)
    
    # Import the module and reload it
    import variable_population_model
    importlib.reload(variable_population_model)  # Reload the entire module
    
    # Now access the class from the reloaded module
    model = variable_population_model.PopulationModel(10, 10, 50, 350)
    return model

def compare_models():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'plot')))
    from plot.compare_models import compare_models
    
    model_1 = get_fixed_model()
    compare_models([model_1])
    
    model_2 = get_variable_model()
    compare_models([model_2])

def subplot_visualizer():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'plot')))
    from plot.subplot_visualizer import subplot_visualizer
    subplot_visualizer(get_fixed_model())

if __name__ == "__main__":
    compare_models()
