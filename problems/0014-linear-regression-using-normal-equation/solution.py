import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round

    X = np.array(X, dtype = float)
    y = np.array(y , dtype = float)

    # X = np.c_[np.ones(X.shape[0]), X]

    theta = np.linalg.inv(X.T @ X) @ X.T @ y

    return np.round(theta, 4)