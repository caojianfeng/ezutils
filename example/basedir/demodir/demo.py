#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from ezutils.files import readlines, writelines


def brother_path(filename): return os.path.join(
    os.path.dirname(__file__), filename)


def write():
    lines = ['hello', 'ezflines']
    writelines(lines, brother_path('cfg.txt'))


def read():
    lines2 = readlines(brother_path('cfg.txt'))
    print(lines2)


if __name__ == "__main__":
    write()
    read()
