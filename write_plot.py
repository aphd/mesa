import argparse
from src.utils.get_model import get_fixed_model, get_variable_model
from plot import compare_tokens, subplot_visualizer

def write_compare_token():
    compare_tokens([get_fixed_model(), get_variable_model()])

def write_subplot_visualizer():
    subplot_visualizer(get_fixed_model())

def main(function_name):
    functions = {
        'write_compare_token': write_compare_token,
        'write_subplot_visualizer': write_subplot_visualizer,
    }

    if function_name in functions:
        functions[function_name]()
    else:
        raise ValueError(f"Function '{function_name}' is not available. Choose from: {', '.join(functions.keys())}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run specific function for plotting.")
    parser.add_argument('function', type=str, help="Name of the function to run (e.g., write_compare_token or write_subplot_visualizer)")
    args = parser.parse_args()
    main(args.function)
