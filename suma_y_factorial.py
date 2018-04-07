# -*- coding: utf-8 -*-
'''
En este programa vamos a modificar para aprender a usar ramas de git.
Let's go!!!!
'''


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact


def suma(num):
    fact = 0
    for i in range(1, num+1):
        fact += i
    return fact

def run():
    try:
        fact = int(input('Ingresa un número: '))
        res_suma = suma(fact)
        res_fact = factorial(fact)
        print('La suma de 1 hasta {} es {}'.format(fact, res_suma))
        print('El factorial de {} es {}'.format(fact, res_fact))
    except ValueError:
        print('Ingresa un valor correcto, solo números enteros!')


if __name__ == '__main__':
    print('Suma de números')
    run()
