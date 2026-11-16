import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here

    X = data

    #standardisation
    x_mean = np.mean(X , axis =0)
    x_std = np.std(X, axis = 0, ddof = 0)

    standardized_data = (X - x_mean) / x_std

    #normalisation

    x_min = np.min(X, axis =0)
    x_max = np.max(X, axis =0)

    normalized_data = (X - x_min) / (x_max - x_min)
    
    return standardized_data, normalized_data