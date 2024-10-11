import argparse
from src.utils.get_model import get_fixed_model, get_variable_model
from plot import compare_tokens_plot, subplot_visualizer, compare_behavior_plot, boxplot_behavior_plot

def compare_tokens():
    compare_tokens_plot([get_fixed_model(), get_variable_model()])

def compare_behavior():
    compare_behavior_plot([get_fixed_model(), get_variable_model()])

def subplots_fixed_model():
    subplot_visualizer(get_fixed_model())

def subplots_variable_model():
    subplot_visualizer(get_variable_model())

def boxplot_behavior():
    boxplot_behavior_plot()

def main(function_name):
    functions = {
        'compare_tokens': compare_tokens,
        'compare_behavior': compare_behavior,
        'subplots_fixed_model': subplots_fixed_model,
        'subplots_variable_model': subplots_variable_model,
        'boxplot_behavior': boxplot_behavior,
    }

    if function_name in functions:
        functions[function_name]()
    else:
        raise ValueError(f"Function '{function_name}' is not available. Choose from: {', '.join(functions.keys())}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run specific function for plotting.")
    parser.add_argument('function', type=str, help="Name of the function to run (e.g., compare_tokens or subplots_fixed_model)")
    args = parser.parse_args()
    main(args.function)
