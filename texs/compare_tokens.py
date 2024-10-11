import os

def compare_tokens(models):
    latex_code = r"""
    \definecolor{myred}{HTML}{f53851}   % Define the red color
    \definecolor{mygreen}{HTML}{c6f56e} % Define the green color
    \begin{tikzpicture}
    \begin{axis}[ 
        xlabel={Time (Days)},
        ylabel={Accumulated Tokens},
        xmin=0, xmax=365,
        ymin=0, ymax=10000,
        grid=major,
        legend pos=north west
    ]""" + "\n"

    for index, model in enumerate(models):
        total_days = model.get_duration()
        token_data = []

        # Run the simulation for the specified number of steps (days)
        for _ in range(total_days):
            model.step()

            # Collect tokens for all agents
            total_tokens = sum(agent.token for agent in model.schedule.agents)
            token_data.append(total_tokens)

        # Determine color and style based on the index
        color = "myred" if index == 0 else "mygreen"
        line_style = "thick" if index == 0 else "thick"
        label = "Fixed Model" if index == 0 else "Variable Model"

        # Add token data for the current model to the LaTeX code
        latex_code += f"""    % {label.lower().replace(" ", "_")}_count
    \\addplot[
        {color}, {line_style}
    ] table {{
        x  y
"""

        for day, total in enumerate(token_data):
            latex_code += f"        {day}  {total}\n"

        latex_code += "    };\n"
        latex_code += f"    \\addlegendentry{{{label}}}\n"

    latex_code += r"""    \end{axis}
\end{tikzpicture}"""

    fn = os.getenv("FN_DIR") + "/compare_tokens.tex"
    with open(fn, "w") as f:
        f.write(latex_code)

    print(f"\033[92mFile created successfully! {fn}\033[0m")

# Example usage
if __name__ == "__main__":
    pass