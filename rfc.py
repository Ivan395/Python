#! /usr/bin/python3
# -*- coding: utf-8 -*-
import curp

def letters(ap):
    letras = [chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if(len(ap) == 13):
        if(ap[0] in letras and ap[1] in letras and ap[2] in letras and ap[3] in letras):
            if(ap[4] in numbers and ap[5] in numbers and ap[6] in numbers and ap[7] in numbers and ap[8] in numbers and ap[9] in numbers):
                st = str('19' + ap[4:6] + '/' + ap[6:8] + '/' + ap[8: 10]).split('/')
                if(ap[10] in numbers or ap[10] in letras and ap[11] in numbers or ap[11] in letras and ap[12] in numbers or ap[12] in letras):
                    return curp.dtval(st)
    return False


def run():
    tmp_rfc = input("Ingresa el RFC: ")
    if(letters(tmp_rfc)):
        print('El RFC es correcto')
    else:
        print('El RFC NO es correcto')


if __name__ == '__main__':
    run()
