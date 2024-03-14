#!/usr/bin/python3
"""
a module that determines if all the locked boxes can be opened
"""

def canUnlockAll(boxes):
    """
      a function with parameter boxes that checks if all boxes can be opened
    """
    set = {0}
    boxLen = len(boxes)

    for i in range(boxLen - 1):
        box = boxes[i]
        for j in range(len(box)):
            index = box[j]
            if (boxes[index] in boxes):
                set.add(index)
                if (len(set) == boxLen and j != i):
                  return True
    return False