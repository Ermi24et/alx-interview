#!/usr/bin/python3
"""Change comes from within"""
import sys


def makeChange(coins, total):
    """returns fewest number of coins needed to meet total"""
    n = len(coins)
    if (total <= 0):
        return (0)
    table = [0 for i in range(total + 1)]

    table[0] = 0

    for i in range(1, total + 1):
        table[i] = sys.maxsize

    for i in range(1, total + 1):
        for j in range(n):
            if (coins[j] <= i):
                sub_sol = table[i - coins[j]]
                if (sub_sol != sys.maxsize and
                    sub_sol + 1 < table[i]):
                    table[i] = sub_sol + 1

    if table[total] == sys.maxsize:
        return (-1)

    return table[total]
