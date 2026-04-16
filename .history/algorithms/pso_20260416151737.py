import random
from utils.fitness import evaluar_ruta
from config import W, C1, C2


def obtener_swaps(ruta1, ruta2):
    """
    Genera una secuencia de swaps para transformar ruta1 en ruta2.
    """
    swaps = []
    r1 = ruta1[:]
    for i in range(len(r1)):
        if r1[i] != ruta2[i]:
            j = r1.index(ruta2[i])
            swaps.append((i, j))
            r1[i], r1[j] = r1[j], r1[i]
    return swaps


def aplicar_swaps(ruta, swaps):
    """
    Aplica una lista de swaps a una ruta.
    """
    nueva = ruta[:]
    for i, j in swaps:
        nueva[i], nueva[j] = nueva[j], nueva[i]
    return nueva


def pso_mejorar(soluciones, distancia, costo, tiempo):
    """
    PSO adaptado a problema discreto usando swaps como "velocidad".
    """

    particulas = []

    # Inicialización
    for s in soluciones:
        particulas.append({
            "ruta": s["ruta"][:],
            "fitness": s["fitness"],
            "pbest": s["ruta"][:],
            "pbest_fit": s["fitness"],
            "velocidad": []  # lista de swaps
        })

    # Mejor global
    gbest = min(particulas, key=lambda x: sum(x["fitness"]))

    for _ in range(10):
        for p in particulas:

            # ===== ECUACIÓN DE VELOCIDAD (ADAPTADA) =====
            # v = w*v + c1*(pBest - x) + c2*(gBest - x)

            swaps_pbest = obtener_swaps(p["ruta"], p["pbest"])
            swaps_gbest = obtener_swaps(p["ruta"], gbest["ruta"])

            nueva_velocidad = []

            # Inercia
            for swap in p["velocidad"]:
                if random.random() < W:
                    nueva_velocidad.append(swap)

            # Componente cognitivo
            for swap in swaps_pbest:
                if random.random() < C1:
                    nueva_velocidad.append(swap)

            # Componente social
            for swap in swaps_gbest:
                if random.random() < C2:
                    nueva_velocidad.append(swap)

            p["velocidad"] = nueva_velocidad

            # ===== ECUACIÓN DE POSICIÓN =====
            # x = x + v

            nueva_ruta = aplicar_swaps(p["ruta"], p["velocidad"])

            nuevo_fit = evaluar_ruta(nueva_ruta, distancia, costo, tiempo)

            # Actualizar estado
            p["ruta"] = nueva_ruta
            p["fitness"] = nuevo_fit

            # Actualizar pBest
            if sum(nuevo_fit) < sum(p["pbest_fit"]):
                p["pbest"] = nueva_ruta[:]
                p["pbest_fit"] = nuevo_fit

        # Actualizar gBest
        gbest = min(particulas, key=lambda x: sum(x["fitness"]))

    return [{"ruta": p["ruta"], "fitness": p["fitness"]} for p in particulas]