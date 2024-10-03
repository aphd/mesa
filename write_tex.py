# write_tex.py
import argparse
from texs import write_agent_behavior, compare_tokens
from src.utils.get_model import get_fixed_model, get_variable_model

def main(function_name):
    # List of available functions mapped to their corresponding actions
    functions = {
        'write_agent_behavior_fixed': lambda: write_agent_behavior(get_fixed_model()),
        'write_agent_behavior_variable': lambda: write_agent_behavior(get_variable_model()),
        'compare_tokens': lambda: compare_tokens([get_fixed_model(), get_variable_model()])
    }
    if function_name in functions:
        functions[function_name]()
    else:
        raise ValueError(f"Function '{function_name}' is not available. Choose from: {', '.join(functions.keys())}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run specific LaTeX generation function.")
    parser.add_argument('function', type=str, help="Name of the function to run (e.g., compare_tokens, write_agent_behavior_variable, write_agent_behavior_fixed)")
    args = parser.parse_args()
    main(args.function)
