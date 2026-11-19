import numpy as np

def to_categorical(x, n_col=None):
    # Your code here
    r = len(x)

    if n_col is None:
        n_col = max(x) + 1

    result = []

    for i in range(r):
        temp = []
        for j in range(n_col):
            if x[i] == j:
                temp.append(1)

            else:
                temp.append(0)

        result.append(temp)
    
    return np.array(result)
