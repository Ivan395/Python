# !/usr/lib64/env python3.6
# -*- coding: utf-8 -*-
from colorama import *
import random


# son bisiestos todos los años divisibles por 4, excluyendo los que sean divisibles por 100, pero no los que sean divisibles por 400.
ENTIDADES_FEDERATIVAS = {
    'aguascalientes': 'AS',
    'baja california': 'BC',
    'baja california sur': 'BS',
    'campeche': 'CC',
    'chiapas': 'CS',
    'chihuahua': 'CH',
    'coahuila': 'CL',
    'colima': 'CM',
    'distrito federal': 'DF',
    'durango': 'DG',
    'guanajuato': 'GT',
    'guerrero': 'GR',
    'hidalgo': 'HG',
    'jalisco': 'JC',
    'mexico': 'MC',
    'michoacan': 'MN',
    'morelos': 'MS',
    'nayarit': 'NT',
    'nuevo leon': 'NL',
    'oaxaca': 'OC',
    'puebla': 'PL',
    'queretaro': 'QT',
    'quintana roo': 'QR',
    'san luis potosi': 'SP',
    'sinaloa': 'SL',
    'sonora': 'SR',
    'tabasco': 'TC',
    'tlaxcala': 'TL',
    'tamaulipas': 'TS',
    'veracruz': 'VZ',
    'yucatan': 'YN',
    'zacatecas': 'ZS'
}


def primer_apellido(last):
    vocales = ['a', 'e', 'i', 'o', 'u']
    st = last[0]
    for i in last[1:]:
        if i in vocales:
            st += i
            break
    return st


def conso(last):
    vocales = ['a', 'e', 'i', 'o', 'u']
    st = ''
    for i in last[1:]:
        if i not in vocales:
            st += i
            break
    return st


def bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 != 0:
            return True
        elif anio % 100 == 0:
            if anio % 400 != 0:
                return False
            else:
                return True
    return False

def last_alpha():
    l = ''
    lis_num = [x for x in range(10)]
    lis_letters = [chr(x) for x in range(65, 91)]
    lis = lis_num + lis_letters
    for i in range(4):
        l += random.choice(lis);
    return l


def validate(fecha):
    fecha = fecha.split('/')
    if ''.join(fecha).isdigit():
        dtval(fecha)
    else:
        return False


def largo(st):
    if len(st) > 3:
        return False
    return True


def dtval(fecha):
    mesese31 = [1, 3, 5, 7, 8, 10, 12]
    anio = int(fecha[0])
    mes = int(fecha[1])
    dia = int(fecha[-1])
    if mes > 0 and mes < 13:
        if mes in mesese31:
            if dia > 0 and dia < 32:
                if anio > 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if mes == 2:
                if anio > 0:
                    if bisiesto(anio):
                        if dia > 0 and dia < 30:
                            return True
                        else:
                            return False
                    else:
                        if dia > 0 and dia < 29:
                            return True
                        else:
                            return False
                else:
                    return False
            else:
                if anio > 0:
                    if dia > 0 and dia < 31:
                        return True
                    else:
                        return False
                else:
                    return False
    else:
        return False


def run():
    last_name = input('Ingresa tu apellido paterno: ').strip()
    while largo(last_name):
        print('Ingresa un nombre Valido')
        last_name = input('Ingresa tu apellido paterno: ').strip()
    second_name = input('Ingresa tu apellido materno: ').strip()
    while largo(second_name):
        print('Ingresa un nombre Valido')
        second_name = input('Ingresa tu apellido materno: ').strip()
    name = input('Ingresa tu numbre: ').strip().split()[0]
    date = input('Ingresa tu fecha de nacimiento (dd/mm/aaaa): ').strip()
    while validate(date):
        print('Fecha invalida, vuelve a intentarlo')
        print('Ejemplo de una fecha valida, 23/03/1963')
        print('Tal cuál como en el ejemplo')
        date = input('Ingresa tu fecha de nacimiento (dd/mm/aaaa): ')
        
    last_name = last_name.split()[-1]
    second_name = second_name.split()[-1]
    tmp1 = conso(last_name).upper()
    tmp2 = conso(second_name).upper()
    tmp3 = conso(name).upper()
    last_name = primer_apellido(last_name)
    date = date.split('/')
    curp = last_name + second_name[0] + name[0] + date[-1][2:] + date[1] + date[0] + last_alpha()
    print('*' * len(curp))
    print(Fore.RED + curp.upper() + Style.RESET_ALL)
    print('*' * len(curp))


if __name__ == '__main__':
    # Tecnicas para la recopilación de datos: entrevista
    run()
