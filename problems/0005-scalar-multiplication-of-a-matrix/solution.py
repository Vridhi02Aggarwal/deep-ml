def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here

    result = []

    k = scalar

    r = len(matrix)
    c = len(matrix[0])

    for i in range(r):
        temp = []
        for j in range(c):
            temp.append(k*matrix[i][j])

        result.append(temp)
        
    return result