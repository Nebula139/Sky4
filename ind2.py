#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = str(input("Введите слово:"))
    a = s[::-1]
    if s == a:
        print("Палиндром")
    else:
        print("Не палиндром")
