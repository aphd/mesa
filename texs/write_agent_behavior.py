
def write_agent_behavior(model):
    good_agents_count = []
    bad_agents_count = []
    duration = model.get_duration()
    for _ in range(duration):
        model.step()
        good_count = sum(1 for agent in model.schedule.agents if agent.behavior == "good")
        bad_count = sum(1 for agent in model.schedule.agents if agent.behavior == "bad")
        good_agents_count.append(good_count)
        bad_agents_count.append(bad_count)

    latex_code = r"""\begin{tikzpicture}
    \begin{axis}[
        xlabel={Time (Days)},
        ylabel={Number of Agents},
        xmin=0, xmax=365,
        ymin=0, ymax=50,
        grid=major,
        legend pos=north west
    ]
    % bad_agents_count
    \addplot[
        red, thick
    ] table {
        x  y"""

    for time, bad_count in zip(range(duration), bad_agents_count):
        latex_code += f"\n        {time}  {bad_count}"

    latex_code += r"""
    };
    \addlegendentry{Bad Agents}

    % good_agents_count
    \addplot[
        green, thick, dashed
    ] table {
        x  y"""

    for time, good_count in zip(range(duration), good_agents_count):
        latex_code += f"\n        {time}  {good_count}"

    latex_code += r"""
    };
    \addlegendentry{Good Agents}
    \end{axis}
    \end{tikzpicture}"""

    fn = "/tmp/output.tex"
    with open(fn, "w") as f: f.write(latex_code)
    print(f"\033[92mFile created successfully! {fn}\033[0m")

if __name__ == "__main__":
    write_agent_behavior()