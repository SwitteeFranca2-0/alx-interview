#!/usr/bin/env python3
"""get status reports"""

import sys

status_code = {}
file_size = 0

i = 0
try:
    for line in sys.stdin:
        i += 1
        file_size += int(line.split()[-1])
        code = line.split()[-2]
        if code not in status_code.keys():
            status_code[code] = 1 
        else:
            status_code[code] += 1
        if i == 10:
            print("File Size: {}".format(file_size))
            stat_code = dict(sorted(status_code.items()))
            for c, i in stat_code.items():
                print("{}: {}".format(c, i))
            i = 0
except KeyboardInterrupt as e:
    print("File Size: {}".format(file_size))
    stat_code = dict(sorted(status_code.items()))
    for c, i in stat_code.items():
        print("{}: {}".format(c, i))
    raise e
    