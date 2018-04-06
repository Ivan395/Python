# !/usr/lib64/bin/env python3.6
# -*- coding: utf-8 -*-
import random


def run():
    a = [x for x in range(1, 53)]
    b = '-'.split() * 52
    for i in range(len(a)):
        rando = random.randint(0, 51)
        if a[rando] in b:
            while a[rando] in b:
                rando = random.randint(0, 51)
            b[i] = a[rando]
        else:
            b[i] = a[rando]
    return b

if __name__ == '__main__':
    print('Bienvenidos sean a mi programa')
    lista = run()
    print(('len: {0}\n{1}'.format(len(lista), lista)))
