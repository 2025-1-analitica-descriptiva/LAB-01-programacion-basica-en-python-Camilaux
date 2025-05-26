"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.read_data import read_data

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    data = read_data()

    datos = {}

    for row in data:
        dic = row[4].split(',')
        for i in dic:
            key, value = i.split(':')
            if key not in datos:
                datos[key] = [int(value), int(value)]
            else:
                datos[key][0] = min(datos[key][0], int(value))
                datos[key][1] = max(datos[key][1], int(value))
    # Ordenar el diccionario por la clave
    datos = sorted(datos.items(), key=lambda x: x[0])
    # Convertir el diccionario a la lista de tuplas
    datos = [(key, value[0], value[1]) for key, value in datos]
    return datos
