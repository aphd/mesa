from src.utils.get_model import get_fixed_model, get_variable_model
from plot.compare_tokens import compare_tokens
from plot.subplot_visualizer import subplot_visualizer

def write_compare_token():
    compare_tokens([get_fixed_model(), get_variable_model()])

def write_subplot_visualizer():
    subplot_visualizer(get_fixed_model())

if __name__ == "__main__":
    # TODO add option to choose amoing different options
    write_compare_token()
    # write_subplot_visualizer()
