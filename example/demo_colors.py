#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from ezutils.colors import rgb2hsv, hsv2rgb


def test():
    h, s, v = rgb2hsv(255, 153, 91)
    print(f"rgb(255,153,51)->hsv({h},{s},{v})")
    r, g, b = hsv2rgb(h, s, v)
    print(f"hsv({h},{s},{v})->rgb({r},{g},{b})")


if __name__ == "__main__":
    test()
