import random
from utils.fitness import evaluar_ruta
from config import *

def swap(ruta):
    i, j = random.sample(range(len(ruta)), 2)
    ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta


def pso_mejorar(soluciones, distancia, costo, tiempo):
    mejores = []

    for s in soluciones:
        ruta = s["ruta"][:]
        mejor_ruta = ruta
        mejor_fit = s["fitness"]

        for _ in range(10):
            nueva = swap(ruta[:])
            fit = evaluar_ruta(nueva, distancia, costo, tiempo)

            if sum(fit) < sum(mejor_fit):
                mejor_ruta = nueva
                mejor_fit = fit

        mejores.append({
            "ruta": mejor_ruta,
            "fitness": mejor_fit
        })

    return mejores