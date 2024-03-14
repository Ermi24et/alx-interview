#!/usr/bin/python3
"""
a module that determines if all the locked boxes can be opened
"""


def canUnlockAll(boxes):
    """
      a function with parameter boxes that checks if all boxes can be opened
    """
    for key in range(1, len(boxes)):
        opened = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                opened = True
                break
        if not opened:
            return False
    return True
