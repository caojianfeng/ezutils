#!/usr/bin/env python3

import time

from ezutils.progress import print_progress

if __name__ == '__main__':
    max = 100
    for i in range(max + 1):
        print_progress( i, max,msg=f"MSG:ABCDEFGHIJKLMNOPQRSTUVWXY({i})")
        time.sleep(0.01)
