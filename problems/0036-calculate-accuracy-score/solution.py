import numpy as np

def accuracy_score(y_true, y_pred):
    # Your code here
    n = len(y_true)

    corr = 0

    for i in range(n):
        if y_pred[i] == y_true[i]:
            corr += 1
    
    acc = corr / n
    
    return acc