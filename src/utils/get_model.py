import sys
import os

width, height, N, duration = 10, 10, 50, 356

def get_fixed_model():
    sys.path.insert(0, variable_path) if (variable_path := os.path.abspath(os.path.join(os.path.dirname(__file__), '../../fixed-incentives-model'))) not in sys.path else None
    import fixed_population_model
    model = fixed_population_model.PopulationModel(width, height, N, duration )
    return model

def get_variable_model():
    sys.path.insert(0, variable_path) if (variable_path := os.path.abspath(os.path.join(os.path.dirname(__file__), '../../variable-incentives-model'))) not in sys.path else None
    import variable_population_model
    model = variable_population_model.PopulationModel(width, height, N, duration )
    return model