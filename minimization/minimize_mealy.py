from automata.mealy_machine import MealyMachine

def minimize_mealy(machine, alphabet):

    states = list(machine.transitions.keys())

    partitions = []
    output_map = {}

    for s in states:
        signature = tuple(machine.transitions[s][a][1] for a in alphabet)

        if signature not in output_map:
            output_map[signature] = []

        output_map[signature].append(s)

    partitions = list(output_map.values())
    changed = True

    while changed:
        changed = False
        new_partitions = []

        for group in partitions:
            subgroup_map = {}

            for state in group:
                signature = []

                for a in alphabet:
                    next_state = machine.transitions[state][a][0]

                    for idx, part in enumerate(partitions):
                        if next_state in part:
                            signature.append(idx)
                            break

                signature = tuple(signature)

                if signature not in subgroup_map:
                    subgroup_map[signature] = []

                subgroup_map[signature].append(state)

            if len(subgroup_map) > 1:
                changed = True

            new_partitions.extend(subgroup_map.values())

        partitions = new_partitions

    minimized = MealyMachine()
    state_map = {}

    for idx, group in enumerate(partitions):
        for state in group:
            state_map[state] = idx

    for idx, group in enumerate(partitions):
        representative = group[0]

        for a in alphabet:
            next_state, output = machine.transitions[representative][a]

            minimized.add_transition(
                idx,
                a,
                state_map[next_state],
                output
            )

    return minimized