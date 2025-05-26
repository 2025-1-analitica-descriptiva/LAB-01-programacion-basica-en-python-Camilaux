"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.read_data import read_data

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    data = read_data()

    registro = {}

    for row in data:
        mes = row[2].split('-')[1]  # Extrae el mes de la fecha
        
        if mes in registro:
            registro[mes] += 1
        else:
            registro[mes] = 1
    # Ordena el diccionario por clave (mes) y convierte a lista de tuplas
    registro_ordenado = sorted(registro.items())
    return registro_ordenado