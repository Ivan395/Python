#! /usr/lib64/env python3
# -*- coding: utf-8 -*-

def validate(mi, ma):
    if int(mi) > int(ma):
        tmp = mi
        mi = ma
        ma = tmp
        return mi, ma
    return int(mi), int(ma)

def run():

    mini = input("Ingresa el número minimo\n")
    mini = mini if mini != '' else 0
    maxi = input("Ingresa el número maximo\n")
    maxi = maxi if maxi != '' else 10
    tmp = validate(int(mini), int(maxi))
    lista = [x for x in range(tmp[0], tmp[1])]
    for i in lista:
        st = ''
        if i % 3 == 0:
            st += 'fizz '
        if i % 5 == 0:
            st += 'bozz'
        if st.strip() != "":
            print('{}: {}'.format(i, st))

if __name__ == '__main__':
    run()
