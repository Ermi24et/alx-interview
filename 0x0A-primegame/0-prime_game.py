#!/usr/bin/python3
"""
Prime Number
"""


def check_prime(n):
    """checks and returns the primes of a number"""
    primes = []
    elemets = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (elemets[prime]):
            primes.append(prime)
            for i in range(prime, n + 1, prime):
                elemets[i] = False
    return primes


def isWinner(x, nums):
    """returns the name of the player that won the most rounds"""
    Ben = Maria = 0
    for i in range(x):
        primes = check_prime(nums[i])
        if (len(primes) % 2 == 0):
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
