#!/usr/bin/python3
""" a module for the pascals triangle """


def pascal_triangle(n):
    """ a function that returns a list of lists of integers
    representing the pascal's triangle of n:
    """
    finalList = []
    if (n <= 0):
        return finalList

    else:
        for i in range(1, n + 1):
            temp = []
            val = 1
            for j in range(1, (i + 1)):
                temp.append(val)
                val = val * (i - j) // j
            finalList.append(temp)
    return finalList
