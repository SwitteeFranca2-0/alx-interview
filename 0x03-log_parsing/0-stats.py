#!/usr/bin/python3
"""get status reports"""

import sys

status_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
               404: 0, 405: 0, 500: 0}
file_size = 0

i = 0


def print_file(dic, file_size):
    print("File Size: {}".format(file_size))
    stat_code = dict(sorted(dic.items()))
    for c, i in stat_code.items():
        if i != 0:
            print("{}: {}".format(c, i))

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            i += 1
            file_size += int(line.split()[-1])
            code = line.split()[-2]
            if code.isnumeric():
                if int(code) in status_code.keys():
                    status_code[int(code)] += 1
            if i == 10:
                print_file(status_code, file_size)
                i = 0
    except KeyboardInterrupt as e:
        print_file(status_code, file_size)
        raise
