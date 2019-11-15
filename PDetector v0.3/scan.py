#!python3

import socket, json

def port_det(host):

    with open('puertos.json') as file:
        puertos = json.load(file)

    linea = [host]
    resultados = [['PUERTO', 'ESTADO', 'SERVICIO']]

    for puerto in puertos:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #nidea que ni como
        conn = sock.connect_ex((str(host), puertos[puerto]))
        if conn == 0:
            linea.append(True)
            resultados.append([puertos[puerto], 'Abierto', puerto]) #puerto, estado, servicio
        else:
            linea.append(False)
        sock.close()

    if True in linea:
        print(f'servicios encontrados en {host}')
        print()
        for lista in resultados:
            print(lista[0],' - ', lista[1],' - ', lista[2])
    else:
        print(f'Host: {host}, no se detecta servicios expuestos')
        print()
    print()

    return linea
