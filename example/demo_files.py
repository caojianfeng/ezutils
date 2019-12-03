#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from ezutils.files import readlines, writelines, readstr, readjson, list_by_ext


def brother_path(filename): return os.path.join(
    os.path.dirname(__file__), filename)


def read_as_lines():
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


def write_as_lines():
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


def read_as_string():
    string = readstr(brother_path('cfg.txt'))
    print(f"read_as_string:\n{string}")


def read_as_json():
    json_obj = readjson(brother_path('cfg.json'))
    print(f"read_as_json: type = {type(json_obj)}")
    images = json_obj["images"]
    for image in images:
        print(f"read_as_json: image = {image}")


def find_pys():
    files = list_by_ext('.', 'py')
    index = 0
    width = len(f"{len(files)}")
    for file in files:
        print(f"[{index:0{width}}] {file}")
        index += 1


if __name__ == "__main__":
    write_as_lines()
    read_as_lines()
    read_as_string()
    read_as_json()
    find_pys()
