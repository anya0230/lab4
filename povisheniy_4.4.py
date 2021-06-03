#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Дано предложение. Найти длину его самого короткого слова.

if __name__ == '__main__':
    s = "Привет мир"
    l = s.split()
    print(len(min(l, key=len)))
