import random
import math

import random
import math


def generar_ciudades(n):
    """
    Genera ciudades distribuidas tipo cuadrícula urbana.
    """

    ciudades = []

    columnas = int(math.sqrt(n))
    espacio = 20

    for i in range(n):
        fila = i // columnas
        columna = i % columnas

        x = columna * espacio + random.uniform(-3, 3)
        y = fila * espacio + random.uniform(-3, 3)

        ciudades.append((x, y))

    return ciudades

def calcular_distancia(ciudades):
    """
    Calcula la distancia entre todas las ciudades usando distancia euclidiana.

    Parámetros:
        ciudades (list): Lista de coordenadas.

    Retorna:
        list[list]: Matriz de distancias.
    """
    n = len(ciudades)
    matriz = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            x1, y1 = ciudades[i]
            x2, y2 = ciudades[j]
            matriz[i][j] = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    return matriz

def generar_costo_tiempo(n):
    """
    Genera matrices de costo y tiempo de forma aleatoria.

    Parámetros:
        n (int): Número de ciudades.

    Retorna:
        tuple: (costo, tiempo)
    """
    costo = [[random.uniform(1, 10) for _ in range(n)] for _ in range(n)]
    tiempo = [[random.uniform(1, 10) for _ in range(n)] for _ in range(n)]

    return costo, tiempo