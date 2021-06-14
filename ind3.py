#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = input("Введите слово:")
    i = int(input(''))
    w = s.replace(s[2], '')
    w = w.replace(w[i], '')
    print(w)
