import random
from utils.fitness import evaluar_ruta


def swap(ruta):
    """
    Realiza un intercambio aleatorio de dos posiciones en la ruta.

    Este operador permite explorar nuevas soluciones en el espacio de búsqueda.

    Parámetros:
        ruta (list): Ruta actual.

    Retorna:
        list: Nueva ruta modificada.
    """
    i, j = random.sample(range(len(ruta)), 2)
    ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta


def pso_mejorar(soluciones, distancia, costo, tiempo):
    """
    Aplica un PSO simplificado para mejorar un conjunto de soluciones.

    Cada solución se trata como una partícula que se ajusta iterativamente
    considerando:
    - Su mejor estado previo (pBest)
    - La mejor solución global (gBest)

    Parámetros:
        soluciones (list): Lista de soluciones (rutas y fitness).
        distancia (list[list]): Matriz de distancias.
        costo (list[list]): Matriz de costos.
        tiempo (list[list]): Matriz de tiempos.

    Retorna:
        list: Lista de soluciones mejoradas.
    """

    # Inicialización de partículas
    particulas = []

    for s in soluciones:
        particulas.append({
            "ruta": s["ruta"][:],
            "fitness": s["fitness"],
            "pbest": s["ruta"][:],
            "pbest_fit": s["fitness"]
        })

    # Mejor solución global (gBest)
    gbest = min(particulas, key=lambda x: sum(x["fitness"]))

    # Iteraciones del proceso de mejora
    for _ in range(10):
        for p in particulas:

            nueva_ruta = p["ruta"][:]

            # Influencia de la mejor solución individual (pBest)
            if random.random() < 0.5:
                nueva_ruta = swap(nueva_ruta)

            # Influencia de la mejor solución global (gBest)
            if random.random() < 0.7:
                nueva_ruta = swap(nueva_ruta)

            nuevo_fit = evaluar_ruta(nueva_ruta, distancia, costo, tiempo)

            # Actualizar estado actual de la partícula
            p["ruta"] = nueva_ruta
            p["fitness"] = nuevo_fit

            # Actualizar mejor solución individual (pBest)
            if sum(nuevo_fit) < sum(p["pbest_fit"]):
                p["pbest"] = nueva_ruta[:]
                p["pbest_fit"] = nuevo_fit

        # Actualizar mejor solución global (gBest)
        gbest = min(particulas, key=lambda x: sum(x["fitness"]))

    # Retornar soluciones mejoradas
    return [{"ruta": p["ruta"], "fitness": p["fitness"]} for p in particulas]