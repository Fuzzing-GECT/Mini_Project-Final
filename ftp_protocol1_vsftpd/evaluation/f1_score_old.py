import random
from oracle.membership_query import membership_query

def evaluate_f1(model,alphabet,tests=400):

    TP=0
    FP=0
    FN=0

    for _ in range(tests):

        seq=tuple(random.choice(alphabet) for _ in range(random.randint(1,8)))

        real=membership_query(seq)

        pred=model.simulate(seq)

        for r,p in zip(real,pred):

            if r==p:
                TP+=1
            else:
                FP+=1
                FN+=1


    precision=TP/(TP+FP) if (TP+FP)>0 else 0
    recall=TP/(TP+FN) if (TP+FN)>0 else 0

    if precision+recall==0:
        f1=0
    else:
        f1=2*precision*recall/(precision+recall)

    return precision,recall,f1
