"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    # Abre el archivo data.csv en modo lectura
    with open('./files/input/data.csv', 'r') as file:
        # Lee todas las líneas del archivo
        lines = file.readlines()

    # Inicializa un diccionario para contar las letras
    counts = {}

    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la coma como separador
        columns = line.split('\t')
        # Toma la primera letra de la primera columna (índice 0)
        letter = columns[0][0]
        # Si la letra ya está en el diccionario, incrementa su contador
        if letter in counts:
            counts[letter] += 1
        # Si no está, inicializa su contador en 1
        else:
            counts[letter] = 1

    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    result = sorted(counts.items())

    print(result)
    print(counts)

    # Retorna la lista de tuplas con las letras y sus conteos
    return result
