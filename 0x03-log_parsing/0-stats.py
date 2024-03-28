#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0


def print_op():
        """
        prints all
        """
        print("File size:", total_file_size)
        for k, v in status_codes.items():
            if v:
                print(f"{k}: {v}")
try:
    for line in sys.stdin:
        line_count += 1
        line = line.split()
        try:
            file_size = int(line[-1])
            total_file_size += file_size
        except (IndexError, ValueError, TypeError):
            continue
        try:
            status_code = int(line[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (IndexError, ValueError, TypeError):
            continue
        if count == 10:
            print_op()
            line_count = 0
    print_op()
except KeyboardInterrupt:
        print_op()
