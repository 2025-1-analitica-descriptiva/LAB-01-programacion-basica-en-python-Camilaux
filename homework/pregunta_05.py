"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.read_data import read_data

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    data = read_data()

    result = {}
    for row in data:
        columna_1 = row[0]
        column_2 = int(row[1])
        
        if columna_1 not in result:
            result[columna_1] = [column_2, column_2]
        else:
            # Actualizar max
            if column_2 > result[columna_1][0]:
                result[columna_1][0] = column_2
            # Actualizar min    
            if column_2 < result[columna_1][1]:
                result[columna_1][1] = column_2

    # Convert the dictionary to the required list format
    result = [(key, value[0], value[1]) for key, value in result.items()]
    result.sort(key=lambda x: x[0])
    return result
