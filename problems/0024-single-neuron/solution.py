import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # Your code here

    probabilities = []

    for i in range(len(features)):
        z = 0
        for j in range(len(features[0])):
            z += features[i][j] * weights[j]
        
        z += bias

        sig = 1 / (1 + math.exp(-z))

        probabilities.append(sig)

    
    error = 0

    for x in range(len(labels)):
        error += (probabilities[x] - labels[x])**2

    mse = error / len(labels)

    return np.round(probabilities ,4), np.round(mse , 4)

