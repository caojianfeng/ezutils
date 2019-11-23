#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from ezutils.files import readlines, writelines


def brother_path(filename): return os.path.join(
    os.path.dirname(__file__), filename)


def read():
    lines1 = readlines(brother_path('cfg.txt'))
    print(f"lines1:{lines1}")
    '''
    lines1:['hello', 'ezflines']
    '''
    lines2 = readlines(brother_path('cfg.txt'), False)
    print(f"lines2:{lines2}")
    '''
    lines2:['hello\n', 'ezflines\n']
    '''


def write():
    lines = ['hello', 'ezflines']
    writelines(lines, brother_path('cfg.txt'))
    '''
    cfg.txt:
    hello
    ezflines

    '''
    writelines(lines, brother_path('cfg_oneline.txt'), False)
    '''
    cfg_oneline.txt:
    helloezflines
    '''


if __name__ == "__main__":
    write()
    read()
