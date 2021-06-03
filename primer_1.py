#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Дано предложение. Все пробелы в нем заменить символом «_».

if __name__ == '__main__':
    s = input("Введите предложение: ")
    r = s.replace(' ', '_')
    print(r)


