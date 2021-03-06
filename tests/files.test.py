#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
from ezutils.files import *

import shutil
import os
import sys


def brother_path(filename): return os.path.join(
    os.path.dirname(__file__), filename)


def delete_file(filename):
    if(os.path.exists(filename)):
        os.remove(filename)


file_temple = brother_path('datas/cfg.txt.bak')
file_json_temple = brother_path('datas/cfg.json.bak')
file_input = brother_path('datas/inputs/cfg.txt')
file_json_input = brother_path('datas/inputs/cfg.json')
file_output1 = brother_path('datas/outputs/log1.txt')
file_output2 = brother_path('datas/outputs/log2.txt')


class TestFiles(unittest.TestCase):
    def setUp(self):
        shutil.copyfile(file_temple, file_input)
        shutil.copyfile(file_json_temple, file_json_input)

    def tearDown(self):
        # delete_file(file_input)
        # delete_file(file_output)
        # delete_file(file_json_input)
        pass

    def test_readlines1(self):
        lines1 = readlines(file_input)
        self.assertEqual(lines1, ['hello', 'ezutils.files'])

    def test_readlines2(self):
        lines1 = readlines(file_input, True)
        self.assertEqual(lines1, ['hello', 'ezutils.files'])

    def test_readlines3(self):
        lines1 = readlines(file_input, False)
        self.assertEqual(lines1, ['hello\n', 'ezutils.files\n'])

    def test_writelines1(self):
        lines = ['hello', 'ezutils.files']
        writelines(lines, file_output1)
        lineso = readlines(file_output1)
        self.assertEqual(lines, lineso)

    def test_writelines2(self):
        lines = ['hello', 'ezutils.files']
        writelines(lines, file_output1, True)
        lineso = readlines(file_output1)
        self.assertEqual(lines, lineso)

    def test_writelines3(self):
        lines = ['hello', 'ezutils.files']
        writelines(lines, file_output2, False)
        lineso = readlines(file_output2)
        self.assertEqual(['helloezutils.files'], lineso)

    def test_readstr(self):
        content = readstr(file_input)
        self.assertEqual(content, 'hello\nezutils.files\n')

    def test_readjson(self):
        json_obj = readjson(file_json_input)
        print(type(json_obj))
        images = json_obj["images"]
        self.assertIs(len(images) > 0, True)


if __name__ == "__main__":
    unittest.main()
