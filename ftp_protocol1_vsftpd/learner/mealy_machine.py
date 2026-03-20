class MealyMachine:

    def __init__(self):
        self.transitions={}
        self.initial_state=0


    def add_transition(self,state,symbol,next_state,output):

        if state not in self.transitions:
            self.transitions[state]={}

        self.transitions[state][symbol]=(next_state,output)


    def simulate(self,input_sequence):

        state=self.initial_state
        outputs=[]

        for symbol in input_sequence:

            if state in self.transitions and symbol in self.transitions[state]:

                next_state,output=self.transitions[state][symbol]

                outputs.append(output)
                state=next_state

            else:
                outputs.append("OFF")

        return outputs


    def export_dot(self,filename):

        dot=[
        "digraph Mealy {",
        "rankdir=LR;",
        "node [shape=circle];"
        ]

        colors={
        "230":"green",
        "530":"red",
        "331":"orange",
        "221":"blue"
        }

        for state,transitions in self.transitions.items():

            for cmd,(next_state,output) in transitions.items():

                color=colors.get(output,"black")

                label=f"{cmd} / {output}"

                dot.append(
                f'{state} -> {next_state} [label="{label}", color="{color}", fontcolor="{color}"];'
                )

        dot.append("}")

        with open(filename,"w") as f:
            f.write("\n".join(dot))
