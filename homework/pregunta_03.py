"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from homework.read_data import read_data


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    data = read_data()
    
    suma = {}
    for renglon in data:
        letra = renglon[0]
        valor = int(renglon[1])
        if letra in suma:
            suma[letra] += valor
        else:
            suma[letra] = valor

    suma_ordenada = sorted(suma.items())
    return suma_ordenada

