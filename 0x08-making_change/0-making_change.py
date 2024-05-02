#!/usr/bin/python3
"""Change comes from within"""
import sys


def makeChange(coins, total):
    """returns fewest number of coins needed to meet total"""
    if total <= 0:
        return (0)
    
    coins = sorted(coins)[::-1]
    i = 0
    for coin in coins:
        if total <= 0:
            break
        while total >= coin:
            total -= coin
            i += 1
    if total:
        return (-1)
    return (i)
