def mealy_to_grammar(machine, alphabet):
    grammar = {}
    
    # Each state becomes a non-terminal
    for state in machine.transitions:
        grammar[f"Q{state}"] = []
    
    # Build productions
    for state, transitions in machine.transitions.items():
        for symbol in alphabet:
            if symbol in transitions:
                next_state, output = transitions[symbol]
                
                # Production rule
                production = f"{symbol} Q{next_state}  [out:{output}]"
                grammar[f"Q{state}"].append(production)
    
    return grammar
