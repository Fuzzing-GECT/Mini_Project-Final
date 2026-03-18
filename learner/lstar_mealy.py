import random
from oracle.membership_query import membership_query
from automata.mealy_machine import MealyMachine

class LStarMealy:

    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.S = [()]
        self.E = [()]
        self.mq_cache = {}

    def table_entry(self, s, e):
        full = s + e

        if not full:
            return "INIT"

        if full not in self.mq_cache:
            self.mq_cache[full] = membership_query(full)

        return self.mq_cache[full][-1]

    def row(self, s):
        return tuple(self.table_entry(s, e) for e in self.E)

    def is_closed(self):
        S_rows = {self.row(s) for s in self.S}

        for s in self.S:
            for a in self.alphabet:
                sa = s + (a,)
                if self.row(sa) not in S_rows:
                    return False, sa

        return True, None

    def is_consistent(self):
        for s1 in self.S:
            for s2 in self.S:
                if s1 != s2 and self.row(s1) == self.row(s2):
                    for a in self.alphabet:
                        if self.row(s1 + (a,)) != self.row(s2 + (a,)):
                            return False, (s1, s2, a)

        return True, None

    def build_hypothesis(self):
        hyp = MealyMachine()
        unique_rows = {}

        for s in self.S:
            r = self.row(s)
            if r not in unique_rows:
                unique_rows[r] = len(unique_rows)

        processed = set()

        for s in self.S:
            r = self.row(s)
            if r in processed:
                continue

            curr = unique_rows[r]

            for a in self.alphabet:
                out = self.table_entry(s, (a,))
                next_row = self.row(s + (a,))
                next_state = unique_rows[next_row]

                hyp.add_transition(curr, a, next_state, out)

            processed.add(r)

        hyp.initial_state = unique_rows[self.row(())]
        return hyp

    def equivalence_query(self, hyp):
        for _ in range(150):
            test = tuple(random.choice(self.alphabet)
                         for _ in range(random.randint(1, 8)))

            if membership_query(test) != hyp.simulate(test):
                return test

        return None

    def run(self):
        while True:

            while True:
                closed, witness = self.is_closed()
                if not closed:
                    self.S.append(witness)
                    continue

                consistent, witness = self.is_consistent()
                if not consistent:
                    s1, s2, a = witness
                    self.E.append((a,))
                    continue

                break

            hyp = self.build_hypothesis()
            ce = self.equivalence_query(hyp)

            if not ce:
                return hyp

            for i in range(len(ce)):
                suffix = ce[i:]
                if suffix not in self.E:
                    self.E.append(suffix)