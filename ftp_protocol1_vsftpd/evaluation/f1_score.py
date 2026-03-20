import random
from oracle.membership_query import membership_query

def evaluate_f1(model, alphabet, tests=400):
    error_responses = ["500", "530", "503"]
    invalid_count=0
    TP = 0
    FP = 0
    FN = 0

    for _ in range(tests):
        
        seq = tuple(random.choice(alphabet) for _ in range(random.randint(1, 8)))

        real = membership_query(seq)
        pred = model.simulate(seq)

        for r, p in zip(real, pred):
            if r == p:
                TP += 1
            else:
                # Decide FP vs FN based on "error vs valid"
                
                # Treat error responses as negative class
                

                if p in error_responses and r not in error_responses:
                    FN += 1   # model said error, real was valid
                    print("FN- Model said not ok , but ok",seq)
                    print("-" * 30)
                    print(f"DEBUG: False Negative found!")
                    print(f"Sequence: {seq}")
                    print(f"Real Server Responses:  {real}")
                    print(f"Learned Model Predicted: {pred}")
                    print("-" * 30)

                elif p not in error_responses and r in error_responses:
                    FP += 1   # model said valid, real was error
                    print("FP- Model said ok , but not ok",seq)

                else:
                    # both wrong but different → count as FP
                    FP += 1
                    print("FP- Model said ok , but not ok",seq)
                    
                    
        for r, p in zip(real, pred):
            if p in error_responses or r in error_responses:
                invalid_count+=1
                break

    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    print("FN",FN)
    print("FP",FP)
    print("invalid count",invalid_count)
    if precision + recall == 0:
        f1 = 0
    else:
        f1 = 2 * precision * recall / (precision + recall)

    return precision, recall, f1
    
    
