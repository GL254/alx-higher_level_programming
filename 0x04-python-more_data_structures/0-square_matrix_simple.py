#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
"""computes the square value of all integers of a matrix."""
new_matrix = matrix.copy()

for i in rnge(len(matrix)):
new_matrix[i] = list(map(lambda num: num**2, matrix[i]))

return (new_matrix)
