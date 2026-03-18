def export_dot(machine, filename="model.dot"):

    dot = [
        "digraph MealyMachine {",
        "  rankdir=LR;",
        "  node [shape=circle];",
        "  start [shape=point];",
        f"  start -> {machine.initial_state};"
    ]

    for state, transitions in machine.transitions.items():
        for cmd, (next_state, output) in transitions.items():
            label = f"{cmd} / {output}"
            dot.append(f'  {state} -> {next_state} [label="{label}"];')

    dot.append("}")

    with open(filename, "w") as f:
        f.write("\n".join(dot))

    print(f"Model saved to {filename}")