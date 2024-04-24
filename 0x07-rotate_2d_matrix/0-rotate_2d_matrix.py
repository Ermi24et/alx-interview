#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """a method that rotate a 2D matrix 90 degrees clockwise """
    temp = matrix[0][0]
    temp1 = matrix[0][1]
    temp2 = matrix[0][2]
    temp3 = matrix[1][2]
    matrix[0][0] = matrix[2][0]
    matrix[0][1] = matrix[1][0]
    matrix[0][2] = temp
    matrix[1][0] = matrix[2][1]
    matrix[1][1] = matrix[1][1]
    matrix[1][2] = temp1
    matrix[2][0] = matrix[2][2]
    matrix[2][1] = temp3
    matrix[2][2] = temp2
