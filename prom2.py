#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def validate_key(ap):
    tmp_key = ''
    while(len(ap) != 2):
        print('Clave incorrecta, largo de la clave maxima es 2')
        tmp_key = input('Ingresa la clave')
    return tmp_key

def validate_number(ap):
    try:
        ap = float(ap)
    except:
        return False
    return True

def del_dot(ap):
    st = ''
    for i in ap:
        if i != '.':
            st += i
        else:
            pass
    return st


def run():
    diccio = dict()
    num_claves = int(input('Ingresa el número de claves a escribir\n'))
    while(num_claves <= 0 or num_claves > 5):
        print('Número incorrecto, minimo 1 y maximo 5')
        num_claves = int(input('Ingresa el número de claves a escribir\n'))
    for i in range(num_claves):
        clave = input('Ingresa una clave\n')
        validate_key(clave)
        valor = float(input('Ingresa un valor para la clave: {}\n'.format(clave)))
        while(not validate_number(valor)):
            print('Ingresa un valor correcto')
            valor = float(input('Ingresa un valor para la clave: {}\n'.format(clave)))
        diccio[clave] = valor
    resul_clave = ''
    resul_valor = ''
    for i in diccio:
        resul_clave += i
        if diccio[i] > 0:
            tmp = del_dot(str(diccio[i]))
            resul_valor += '+{}'.format(tmp.zfill(9))
        else:
            sign = str(diccio[i])[0]
            tmp = del_dot(str(diccio[i])[1:])
            resul_valor += '{}{}'.format(sign, tmp.zfill(9))
    print('{} --> {}'.format(resul_clave, resul_valor))


if __name__ == '__main__':
    run()
