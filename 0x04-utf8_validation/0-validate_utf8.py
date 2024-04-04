#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """a method that determines if a given data set represents a valid UTF-8
    encoding"""
    count_ = 0

    for byte in data:
        if count_ == 0:
            if byte >> 3 == 0b11110:
                count_ = 3
            elif byte >> 4 == 0b1110:
                count_ = 2
            elif byte >> 5 == 0b110:
                count_ = 1
            elif byte >> 7 == 0b0:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            count_ -= 1

    return count_ == 0
