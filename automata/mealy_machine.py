class MealyMachine:
    def __init__(self):
        self.transitions = {}
        self.initial_state = 0

    def add_transition(self, state, symbol, next_state, output):
        if state not in self.transitions:
            self.transitions[state] = {}
        self.transitions[state][symbol] = (next_state, output)

    def simulate(self, input_sequence):
        state = self.initial_state
        outputs = []

        for symbol in input_sequence:
            if state in self.transitions and symbol in self.transitions[state]:
                next_state, output = self.transitions[state][symbol]
                outputs.append(output)
                state = next_state
            else:
                outputs.append("OFF")

        return outputs