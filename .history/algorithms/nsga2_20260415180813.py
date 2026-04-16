import random
from utils.fitness import evaluar_ruta
from utils.pareto import clasificar_pareto
from config import *

# =========================
# CREACIÓN DE INDIVIDUO
# =========================
def crear_individuo(n):
    """Genera una ruta aleatoria."""
    ruta = list(range(n))
    random.shuffle(ruta)
    return ruta

# =========================
# CREACIÓN DE POBLACIÓN
# =========================
def crear_poblacion(n, size):
    """Genera la población inicial."""
    return [crear_individuo(n) for _ in range(size)]

# =========================
# EVALUACIÓN DE POBLACIÓN
# =========================
def evaluar_poblacion(poblacion, distancia, costo, tiempo):
    """Evalúa cada individuo con la función de fitness."""
    individuos = []
    for ruta in poblacion:
        fitness = evaluar_ruta(ruta, distancia, costo, tiempo)
        individuos.append({
            "ruta": ruta,
            "fitness": fitness
        })
    return individuos

# =========================
# CRUCE
# =========================
def cruce(padre1, padre2):
    """Combina dos individuos para generar uno nuevo."""
    punto = random.randint(1, len(padre1)-2)
    hijo = padre1[:punto]

    for gen in padre2:
        if gen not in hijo:
            hijo.append(gen)

    return hijo

# =========================
# MUTACIÓN
# =========================
def mutacion(ruta):
    """Realiza un intercambio aleatorio en la ruta."""
    if random.random() < PROB_MUTACION:
        i, j = random.sample(range(len(ruta)), 2)
        ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta

# =========================
# GENERAR NUEVA POBLACIÓN
# =========================
def generar_nueva_poblacion(poblacion):
    """Genera nueva población aplicando cruce y mutación."""
    nueva = []

    if len(poblacion) < 2:
        return [poblacion[0]["ruta"][:] for _ in range(POBLACION_SIZE)]

    while len(nueva) < POBLACION_SIZE:
        p1, p2 = random.sample(poblacion, 2)
        hijo = cruce(p1["ruta"], p2["ruta"])
        hijo = mutacion(hijo)
        nueva.append(hijo)

    return nueva

# =========================
# ALGORITMO NSGA-II
# =========================
def nsga2(n, distancia, costo, tiempo):
    """
    Ejecuta NSGA-II con elitismo y evaluación multiobjetivo.
    """

    poblacion = crear_poblacion(n, POBLACION_SIZE)
    historial = []

    for _ in range(GENERACIONES):

        # Evaluación
        evaluados = evaluar_poblacion(poblacion, distancia, costo, tiempo)

        # Clasificación por Pareto
        frentes = clasificar_pareto(evaluados)
        mejor_frente = frentes[0]

        # Registro de convergencia
        historial.append(min(f["fitness"][0] for f in mejor_frente))

        # =========================
        # ELITISMO
        # =========================
        
        elite = mejor_frente
        elite = sorted(elite, key=lambda x: sum(x["fitness"]))

        nueva = generar_nueva_poblacion(evaluados)

        elite_rutas = [e["ruta"] for e in elite]

        if len(elite_rutas) >= POBLACION_SIZE:
            poblacion = elite_rutas[:POBLACION_SIZE]
        else:
            poblacion = elite_rutas + nueva[:POBLACION_SIZE - len(elite_rutas)]

    return frentes[0], historial