#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
from ezutils.colors import *


class TestColors(unittest.TestCase):
    def test_rgb2hsv(self):
        h, s, v = rgb2hsv(255, 153, 91)
        print("hsv:", h, s, v)

    def test_hsv2rgb(self):
        r, g, b = hsv2rgb(90, 0.5, 0.5)
        print("rgb", r, g, b)

    def test_both(self):
        h, s, v = rgb2hsv(255, 153, 91)
        r, g, b = hsv2rgb(h, s, v)
        self.assertEqual((r, g, b), (255, 153, 91))
        print("rgb:", r, g, b)


if __name__ == "__main__":
    unittest.main()
