from learner.mealy_machine import MealyMachine

def minimize_mealy(machine,alphabet):

    states=list(machine.transitions.keys())

    partitions=[set(states)]

    changed=True

    while changed:

        changed=False
        new_partitions=[]

        for group in partitions:

            splitter={}

            for state in group:

                signature=[]

                for a in alphabet:

                    if a in machine.transitions.get(state,{}):

                        next_state,output=machine.transitions[state][a]

                        next_group=None

                        for i,g in enumerate(partitions):

                            if next_state in g:
                                next_group=i
                                break

                        signature.append((output,next_group))

                    else:

                        signature.append(("OFF",None))

                signature=tuple(signature)

                if signature not in splitter:
                    splitter[signature]=set()

                splitter[signature].add(state)

            if len(splitter)>1:
                changed=True

            new_partitions.extend(splitter.values())

        partitions=new_partitions


    state_map={}

    for i,group in enumerate(partitions):

        for state in group:

            state_map[state]=i

    minimized=MealyMachine()

    for state in states:

        for a,(next_state,output) in machine.transitions.get(state,{}).items():

            minimized.add_transition(
            state_map[state],
            a,
            state_map[next_state],
            output
            )

    minimized.initial_state=state_map[machine.initial_state]

    return minimized
