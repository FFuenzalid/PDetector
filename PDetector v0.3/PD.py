#!python3

def run():
    input = sys.argv[-1]

    if re.search(r'/\d+$', input) is None:
        tosave = port_det(input)
    else:
        network = ip_network(input)
        tosave = []
        for ip in network:
            linea = port_det(ip)
            tosave.append(linea)

    if '-c' in sys.argv:
        pass
    else:
        with open(f'{os.getcwd()}/Pdetector {asctime()}.csv', 'a+', newline='\n') as savefile:
            writer = csv.writer(savefile, quoting=csv.QUOTE_ALL)

            with open('puertos.json') as file:
                puertos = json.load(file)

            #primera linea o encabezado
            primera_linea = ['Host']
            for puerto in puertos:
                primera_linea.append(puerto)

            #lineas de informacion sobre los hosts
            writer.writerow(primera_linea)
            for list in tosave:
                writer.writerow(list)

            print(f'Archivo Guardado en : {os.getcwd()}/Pdetector {asctime()}.csv')

import csv, json, os, sys, re
from ipaddress import *
from time import asctime
from scan import port_det

if len(sys.argv) == 1:
    print('usage: python PDetector.py [OPTIONS] [ip or range]')
    print('[OPTIONS]')
    print('-c               para no guardar ningun archivo')
else:
    print()
    print('---------------------')
    print('Detector de puertos')
    print('---------------------')
    print(f'Objetivo: {sys.argv[-1]}')
    print('---------------------')
    print()
    run()
