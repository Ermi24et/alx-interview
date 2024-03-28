#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

total_file_size = 0
status_code_counts = {status_code: 0 for status_code in status_codes}
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        if len(parts) != 7 or parts[2] != "GET" or parts[3] != "/projects/260" or parts[4] != "HTTP/1.1":
            continue

        file_size = int(parts[-1])
        status_code = int(parts[-2])

        total_file_size += file_size

        if status_code in status_codes:
            status_code_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print("Total file size:", total_file_size)
            for code in sorted(status_codes):
                if status_code_counts[code] > 0:
                    print(f"{code}: {status_code_counts[code]}")
                print()

except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting...")

print("Total file size:", total_file_size)
for code in sorted(status_codes):
    if status_code_counts[code] > 0:
        print(f"{code}: {status_code_counts[code]}")

    match = regex.match(line)
    total = 0
    if match:
        ip_address = match.group(1)
        date = match.group(2)
        status_code = match.group(3)
        file_size = match.group(4)
        total += file_size

        print(f"File size: {total}")
        print(f"{status_code}: ")

