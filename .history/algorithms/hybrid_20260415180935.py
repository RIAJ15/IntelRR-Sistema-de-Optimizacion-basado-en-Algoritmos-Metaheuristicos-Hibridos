from algorithms.nsga2 import nsga2
from algorithms.pso import pso_mejorar

# =========================
# MODELO HÍBRIDO
# =========================
def modelo_hibrido(n, distancia, costo, tiempo):
    """
    Ejecuta el modelo híbrido NSGA-II + PSO.

    Flujo:
    1. Se obtiene un conjunto de soluciones con NSGA-II.
    2. Se refinan esas soluciones utilizando PSO.

    Parámetros:
        n (int): Número de ciudades.
        distancia (matrix): Matriz de distancias.
        costo (matrix): Matriz de costos.
        tiempo (matrix): Matriz de tiempos.

    Retorna:
        tuple:
            - soluciones mejoradas
            - historial de convergencia
    """
    # =========================
    # FASE 1: NSGA-II
    # =========================
    frente, historial = nsga2(n, distancia, costo, tiempo)

    # =========================
    # FASE 2: PSO (REFINAMIENTO)
    # =========================
    mejorado = pso_mejorar(frente, distancia, costo, tiempo)

    return mejorado, historial