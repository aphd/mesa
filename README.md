# mesa

```
source venv/bin/activate
export FN_DIR=/Users/$(whoami)/github/aphd/environment-centric-dashboard-paper/figures
python -m pip list

python write_plot.py compare_tokens
python write_plot.py subplots_fixed_model
python write_plot.py subplots_variable_model
python write_plot.py compare_behavior
python write_plot.py boxplot_behavior

python write_tex.py compare_tokens
python write_tex.py agent_behavior_fixed_model
python write_tex.py agent_behavior_variable_model
python write_tex.py compare_behavior

```