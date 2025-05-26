"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.read_data import read_data

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    data = read_data()

    result = {}

    for row in data:
        key = row[3].split(',')
        value = int(row[1])

        for k in key:

            if k not in result:
                result[k] = 0
            result[k] += value

    # Ordenar el diccionario por las claves
    sorted_result = dict(sorted(result.items()))

    return sorted_result
