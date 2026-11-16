import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method

    o_row = len(a)
    o_col = len(a[0])

    n_row = new_shape[0]
    n_col = new_shape[1]

    if o_row * o_col != n_row * n_col:
        return []

    lists = []

    for i in range(o_row):
        for j in range(o_col):
            lists.append(a[i][j])

    result = []

    for i in range(n_row):
        temp = []
        for j in range(n_col):
            temp.append(lists[i*n_col + j])

        result.append(temp)

    return result
    # return reshaped_matrix