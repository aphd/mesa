import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'texs')))
import texs


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

if __name__ == "__main__":
    # plot.run_all(get_fixed_model())
    texs.run_all(get_variable_model())
