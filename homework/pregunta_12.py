"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.read_data import read_data

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    data = read_data()

    result = {}

    for row in data:
        key = row[0]
        value = row[4].split(',')
        for v in value:
            num = int(v.split(':')[1])
            if key not in result:
                result[key] = 0
            result[key] += num


    # Ordenar el diccionario por las claves
    sorted_result = dict(sorted(result.items()))

    return sorted_result


print(pregunta_12())