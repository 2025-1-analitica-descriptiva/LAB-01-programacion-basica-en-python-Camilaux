"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.read_data import read_data

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    data = read_data()
    result = []
    
    for row in data:
        letter = row[0]
        column_4 = row[3].split(',')
        column_5 = row[4].split(',')
    
        count_col4 = len(column_4) if column_4 else 0
        count_col5 = len(column_5) if column_5 else 0
        result.append((letter, count_col4, count_col5))
    
    return result
