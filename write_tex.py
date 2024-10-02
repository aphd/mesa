from texs.write_agent_behavior import write_agent_behavior
from src.utils.get_model import get_fixed_model, get_variable_model

if __name__ == "__main__":
    # write_agent_behavior(get_fixed_model())
    write_agent_behavior(get_variable_model())
