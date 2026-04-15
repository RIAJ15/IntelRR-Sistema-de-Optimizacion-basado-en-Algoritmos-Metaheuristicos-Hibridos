from algorithms.nsga2 import nsga2
from algorithms.pso import pso_mejorar

def modelo_hibrido(n, distancia, costo, tiempo):
    frente, historial = nsga2(n, distancia, costo, tiempo)

    mejorado = pso_mejorar(frente, distancia, costo, tiempo)

    return mejorado, historial