from config.settings import ALPHABET
from learner.lstar import LStarMealy
from algorithms.minimization import minimize_mealy
from evaluation.f1_score import evaluate_f1
from model_to_grammar import print_grammar




if __name__=="__main__":

    print("[!] Starting Real-World L* Learning on Port 21...")

    learner=LStarMealy(ALPHABET)

    model=learner.run()

    model.export_dot("Before_new.dot")

    print("Before minimisation- states:",len(model.transitions))

    min_model=minimize_mealy(model,ALPHABET)

    print("Minimized states:",len(min_model.transitions))

    min_model.export_dot("After_min_last.dot")
    
    #print_grammar(model)

    precision,recall,f1=evaluate_f1(min_model,ALPHABET)

    print("Precision",precision)
    print("Recall",recall)
    print("F1 Score",f1)

    print("[+] Done!")
