#!/usr/bin/python3
"""N queens"""
import sys

N = sys.argv
if len(N) != 2:
    print(f"Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

k = int(sys.argv[1])


def queens(k, i=0, a=[], b=[], c=[]):
    """discovering all possible positions"""
    if i < k:
        for j in range(k):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(k, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solution(k):
    """a final solution"""
    buf = []
    i = 0
    for sol in queens(k, 0):
        for sol1 in sol:
            buf.append([i, sol1])
            i += 1
        print(buf)
        buf = []
        i = 0


solution(k)
