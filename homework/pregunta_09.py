"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.read_data import read_data

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    data = read_data()

    result = {}
    for row in data:
        key = row[4].split(',')

        for k in key:
            separated_key = k.split(':')[0]
            if separated_key not in result:
                result[separated_key] = 1
            else:
                result[separated_key] += 1
    
    # ordenar
    result = dict(sorted(result.items(), key=lambda item: item[0]))
        
    return result
