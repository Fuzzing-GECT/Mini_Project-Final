# model_to_grammar.py

def clean_symbol(symbol):
    """
    Extract only command name (first word)
    Example:
    'USER anonymous' -> 'USER'
    'REST 0' -> 'REST'
    """
    return symbol.split()[0]


def model_to_grammar(model):

    productions = {}

    # collect all states (including next_state)
    states = set(model.transitions.keys())

    for state in model.transitions:
        for _, (next_state, _) in model.transitions[state].items():
            states.add(next_state)

    for state in states:

        lhs = f"S{state}"

        if lhs not in productions:
            productions[lhs] = set()   # use set to avoid duplicates

        if state in model.transitions:

            for symbol, (next_state, output) in model.transitions[state].items():

                cmd = clean_symbol(symbol)   # only command name
                rhs = f"{cmd} S{next_state}"

                productions[lhs].add(rhs)

    return productions


def print_grammar(model, max_rules_per_state=8):

    productions = model_to_grammar(model)

    start_symbol = f"S{model.initial_state}"
    print(f"Start Symbol: {start_symbol}\n")

    for lhs in sorted(productions.keys()):

        rules = list(productions[lhs])

        # limit rules for readability
        rules = rules[:max_rules_per_state]

        rhs = " | ".join(rules)

        if len(productions[lhs]) > max_rules_per_state:
            rhs += " | ..."

        print(f"{lhs} -> {rhs}")


def save_grammar(model, filename="grammar.txt", max_rules_per_state=8):

    productions = model_to_grammar(model)

    with open(filename, "w") as f:

        start_symbol = f"S{model.initial_state}"
        f.write(f"Start Symbol: {start_symbol}\n\n")

        for lhs in sorted(productions.keys()):

            rules = list(productions[lhs])
            rules = rules[:max_rules_per_state]

            rhs = " | ".join(rules)

            if len(productions[lhs]) > max_rules_per_state:
                rhs += " | ..."

            f.write(f"{lhs} -> {rhs}\n")
