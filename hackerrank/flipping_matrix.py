# accessing columns in array
# Pain in the ass in python. Trivial in numpy

import numpy as np

def flippingMatrix(matrix):
    # Write your code here
    for i in range(2*n): # Go over only half the rows
        if sum(matrix[i][:n]) < sum(matrix[i][n:]):
            # Flip
            temp = matrix[i][:n]
            matrix[i][:n] = matrix[i][n:]
            matrix[i][n:] = temp
    # Columns
    sum_up = 0
    for i in range(n): # Go over only half the rows
        if sum([row[i] for row in matrix][:n]) < sum([row[i] for row in matrix][n:]):
            # Flip
            # for row in matrix:
            temp = [row[i] for row in matrix][:n]
            for j in range(n):
                matrix[]
            matrix[:n][i] = matrix[n:][i]
            matrix[n:][i] = temp
    # print(matrix)
    sumc = 0
    for i in range(n):
        for j in range(n):
            sumc += matrix[i][j]

    return sumc


if __name__ == '__main__':
    q = 1
    n = 2
    print(flippingMatrix([[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]))
