#!/usr/bin/python3
'''Reads stdin line by line and computes metrics'''


import sys


status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
total = 0
count = {code: 0 for code in status_codes}
try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1

        ip, status_code, file_size = line.split(' ')[0], line.split(' ')[-2], line.split(' ')[-1]
        total += int(file_size)
        if status_code in status_codes:
            counts[status_code] += 1
        if line_count % 10 == 0:
            print(f'File size: {total}')
            for code in sorted(count.keys()):
                if count[code] > 0:
                    print(f'{code}: {count[code]}')
except KeyboardInterrupt:
    print(f'Total file size: {total}')
