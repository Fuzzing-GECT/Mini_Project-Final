from config import ALPHABET
from learner.lstar_mealy import LStarMealy
from minimization.minimize_mealy import minimize_mealy
from visualization.export_dot import export_dot
from minimization.grammar import mealy_to_grammar
import random
from oracle.membership_query import membership_query

if __name__ == "__main__":

    learner = LStarMealy(ALPHABET)
    model = learner.run()

    print("\n--- BEFORE MINIMIZATION ---")
    print(model.transitions)

    export_dot(model, "before.dot")

    min_model = minimize_mealy(model, ALPHABET)

    print("\n--- AFTER MINIMIZATION ---")
    print(min_model.transitions)
    grammar = mealy_to_grammar(min_model, ALPHABET)

    print("\n--- GENERATED GRAMMAR ---")
    for non_terminal, productions in grammar.items():
       for p in productions:
         print(f"{non_terminal} → {p}")
    export_dot(min_model, "ftp_learned_model.dot")


def evaluate_f1(model, alphabet, num_tests=200, max_len=10):

    y_true = []
    y_pred = []

    for _ in range(num_tests):

        seq = tuple(random.choice(alphabet)
                    for _ in range(random.randint(1, max_len)))

        # real system output
        real_outputs = membership_query(seq)

        # learned model output
        pred_outputs = model.simulate(seq)

        # compare outputs
        for r, p in zip(real_outputs, pred_outputs):
            y_true.append(r)
            y_pred.append(p)

    return compute_f1_manual(y_true, y_pred)


def compute_f1_manual(y_true, y_pred):

    labels = set(y_true) | set(y_pred)
    f1_scores = []

    for label in labels:

        tp = sum((yt == label and yp == label)
                 for yt, yp in zip(y_true, y_pred))

        fp = sum((yt != label and yp == label)
                 for yt, yp in zip(y_true, y_pred))

        fn = sum((yt == label and yp != label)
                 for yt, yp in zip(y_true, y_pred))

        if tp == 0:
            f1_scores.append(0)
            continue

        precision = tp / (tp + fp)
        recall = tp / (tp + fn)

        if precision + recall == 0:
            f1_scores.append(0)
        else:
            f1_scores.append(2 * precision * recall / (precision + recall))

    return sum(f1_scores) / len(f1_scores)

print("\n--- EVALUATION ---")

f1 = evaluate_f1(min_model, ALPHABET)

print("F1 Score:", f1)

