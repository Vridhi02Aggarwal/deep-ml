import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here

    scores = np.array(scores , dtype = float)

    #numerical stability
    exp_z = np.exp(scores - np.max(scores))

    #probab

    soft_z = exp_z / np.sum(exp_z)
    
    return soft_z