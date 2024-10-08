def compare_behavior_tex(models):
    latex_code = r"""\begin{tikzpicture}
    \begin{axis}[ 
        xlabel={Time (Days)},
        ylabel={Number of Agents},
        xmin=0, xmax=365,
        ymin=0, ymax=10000,
        grid=major,
        legend pos=north west
    ]""" + "\n"

    for index, model in enumerate(models):
        total_days = model.get_duration()
        bad_agents_count = []

        # Run the simulation for the specified number of steps (days)
        for _ in range(total_days):
            model.step()
            bad_count = sum(1 for agent in model.schedule.agents if agent.behavior == "bad")
            bad_agents_count.append(bad_count)

        # Determine color and style based on the index
        color = "red" if index == 0 else "green"
        line_style = "thick" if index == 0 else "thick, dashed"
        label = "Fixed Model" if index == 0 else "Variable Model"

        # Add token data for the current model to the LaTeX code
        latex_code += f"""    % {label.lower().replace(" ", "_")}_count
    \\addplot[
        {color}, {line_style}
    ] table {{
        x  y
"""

        for day, total in enumerate(bad_agents_count):
            latex_code += f"        {day}  {total}\n"

        latex_code += "    };\n"
        latex_code += f"    \\addlegendentry{{{label}}}\n"

    latex_code += r"""    \end{axis}
\end{tikzpicture}"""

    fn = "/tmp/output.tex"
    with open(fn, "w") as f:
        f.write(latex_code)

    print(f"\033[92mFile created successfully! {fn}\033[0m")

# Example usage
if __name__ == "__main__":
    pass