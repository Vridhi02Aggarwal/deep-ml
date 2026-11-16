def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []

    r = len(matrix)
    c = len(matrix[0])

    if mode == "row":
        for i in range(r):
            temp = 0
            for j in range(c):
                temp += matrix[i][j]
            means.append(temp/c) 

    if mode == "column":
        for j in range(c):
            temp = 0
            for i in range(r):
                temp += matrix[i][j]
            means.append(temp/r) 
    
    return means