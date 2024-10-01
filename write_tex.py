import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'texs')))
import texs


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

if __name__ == "__main__":
    # plot.run_all(get_fixed_model())
    texs.run_all(get_variable_model())
