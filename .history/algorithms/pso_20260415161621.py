import random
from utils.fitness import evaluar_ruta

def swap(ruta):
    i, j = random.sample(range(len(ruta)), 2)
    ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta


def pso_mejorar(soluciones, distancia, costo, tiempo):
    """
    PSO simplificado con:
    - mejor local (pBest)
    - mejor global (gBest)
    """

    # Inicializar partículas
    particulas = []

    for s in soluciones:
        particulas.append({
            "ruta": s["ruta"][:],
            "fitness": s["fitness"],
            "pbest": s["ruta"][:],
            "pbest_fit": s["fitness"]
        })

    # Encontrar mejor global
    gbest = min(particulas, key=lambda x: sum(x["fitness"]))

    # Iteraciones PSO
    for _ in range(10):
        for p in particulas:

            nueva_ruta = p["ruta"][:]

            # Influencia propia (pBest)
            if random.random() < 0.5:
                nueva_ruta = swap(nueva_ruta)

            # Influencia global (gBest)
            if random.random() < 0.7:
                nueva_ruta = swap(nueva_ruta)

            nuevo_fit = evaluar_ruta(nueva_ruta, distancia, costo, tiempo)

            # Actualizar posición actual
            p["ruta"] = nueva_ruta
            p["fitness"] = nuevo_fit

            # Actualizar mejor personal
            if sum(nuevo_fit) < sum(p["pbest_fit"]):
                p["pbest"] = nueva_ruta[:]
                p["pbest_fit"] = nuevo_fit

        # Actualizar mejor global
        gbest = min(particulas, key=lambda x: sum(x["fitness"]))

    return [{"ruta": p["ruta"], "fitness": p["fitness"]} for p in particulas]