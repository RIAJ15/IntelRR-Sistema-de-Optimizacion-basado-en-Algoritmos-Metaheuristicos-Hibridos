import random
from utils.fitness import evaluar_ruta
from utils.pareto import clasificar_pareto
from config import *

def crear_individuo(n):
    ruta = list(range(n))
    random.shuffle(ruta)
    return ruta


def crear_poblacion(n, size):
    return [crear_individuo(n) for _ in range(size)]


def evaluar_poblacion(poblacion, distancia, costo, tiempo):
    individuos = []
    for ruta in poblacion:
        fitness = evaluar_ruta(ruta, distancia, costo, tiempo)
        individuos.append({
            "ruta": ruta,
            "fitness": fitness
        })
    return individuos


def cruce(padre1, padre2):
    punto = random.randint(1, len(padre1)-2)
    hijo = padre1[:punto]

    for gen in padre2:
        if gen not in hijo:
            hijo.append(gen)

    return hijo


def mutacion(ruta):
    if random.random() < PROB_MUTACION:
        i, j = random.sample(range(len(ruta)), 2)
        ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta


def generar_nueva_poblacion(poblacion):
    nueva = []

    if len(poblacion) < 2:
        return [poblacion[0]["ruta"][:] for _ in range(POBLACION_SIZE)]

    while len(nueva) < POBLACION_SIZE:
        p1, p2 = random.sample(poblacion, 2)
        hijo = cruce(p1["ruta"], p2["ruta"])
        hijo = mutacion(hijo)
        nueva.append(hijo)

    return nueva


def nsga2(n, distancia, costo, tiempo):
    poblacion = crear_poblacion(n, POBLACION_SIZE)
    historial = []

    for _ in range(GENERACIONES):

        evaluados = evaluar_poblacion(poblacion, distancia, costo, tiempo)
        frentes = clasificar_pareto(evaluados)

        mejor_frente = frentes[0]

        # Guardamos mejor fitness (distancia)
        historial.append(min(f["fitness"][0] for f in mejor_frente))

        # IMPORTANTE: usar TODA la población
        poblacion = generar_nueva_poblacion(evaluados)

    return frentes[0], historial