import random
import math

def generar_ciudades(n):
    """
    Genera n ciudades con coordenadas aleatorias.
    
    Retorna:
        lista de tuplas (x, y)
    """
    ciudades = []
    for _ in range(n):
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        ciudades.append((x, y))
    return ciudades


def calcular_distancia(ciudades):
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
    Genera matrices simuladas de costo y tiempo
    """
    costo = [[random.uniform(1, 10) for _ in range(n)] for _ in range(n)]
    tiempo = [[random.uniform(1, 10) for _ in range(n)] for _ in range(n)]

    return costo, tiempo