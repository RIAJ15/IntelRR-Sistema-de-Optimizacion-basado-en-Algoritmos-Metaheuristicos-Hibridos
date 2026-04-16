import random
from utils.fitness import evaluar_ruta
from utils.pareto import clasificar_pareto
from config import *

def crear_individuo(n):
    """
    Genera un individuo (ruta) como una permutación aleatoria de ciudades.
    """
    ruta = list(range(n))
    random.shuffle(ruta)
    return ruta

def crear_poblacion(n, size):
    """
    Genera una población inicial de individuos.
    """
    return [crear_individuo(n) for _ in range(size)]

def evaluar_poblacion(poblacion, distancia, costo, tiempo):
    """
    Evalúa todos los individuos de la población usando la función de fitness.
    """
    individuos = []
    for ruta in poblacion:
        fitness = evaluar_ruta(ruta, distancia, costo, tiempo)
        individuos.append({
            "ruta": ruta,
            "fitness": fitness
        })
    return individuos

def cruce(padre1, padre2):
    """
    Operador de cruce.

    Combina dos rutas generando un nuevo individuo, preservando el orden
    y evitando duplicados.
    """
    punto = random.randint(1, len(padre1)-2)
    hijo = padre1[:punto]

    for gen in padre2:
        if gen not in hijo:
            hijo.append(gen)

    return hijo

def mutacion(ruta):
    """
    Operador de mutación.

    Realiza un intercambio aleatorio de dos posiciones en la ruta,
    introduciendo variabilidad en la población.
    """
    if random.random() < PROB_MUTACION:
        i, j = random.sample(range(len(ruta)), 2)
        ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta

def generar_nueva_poblacion(poblacion):
    """
    Genera una nueva población a partir de individuos existentes
    aplicando cruce y mutación.
    """
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
    """
    Ejecuta el algoritmo NSGA-II.

    Flujo general:
    1. Inicializa la población.
    2. Evalúa las soluciones.
    3. Clasifica por dominancia de Pareto.
    4. Aplica operadores genéticos.
    5. Preserva las mejores soluciones (elitismo).
    6. Repite por varias generaciones.

    Retorna:
        - Frente de Pareto final.
        - Historial de convergencia.
    """

    poblacion = crear_poblacion(n, POBLACION_SIZE)
    historial = []

    for _ in range(GENERACIONES):

        # Evaluación de la población
        evaluados = evaluar_poblacion(poblacion, distancia, costo, tiempo)

        # Clasificación por frentes de Pareto
        frentes = clasificar_pareto(evaluados)
        mejor_frente = frentes[0]

        # Registro de convergencia (mejor valor)
        historial.append(min(f["fitness"][0] for f in mejor_frente))

        # =========================
        # ELITISMO
        # =========================
        
        # Se conservan las mejores soluciones del frente de Pareto
        elite = mejor_frente

        # Orden por calidad (suma de objetivos)
        elite = sorted(elite, key=lambda x: sum(x["fitness"]))

        # Generación de nueva población
        nueva = generar_nueva_poblacion(evaluados)

        elite_rutas = [e["ruta"] for e in elite]

        # Reemplazo elitista
        if len(elite_rutas) >= POBLACION_SIZE:
            poblacion = elite_rutas[:POBLACION_SIZE]
        else:
            poblacion = elite_rutas + nueva[:POBLACION_SIZE - len(elite_rutas)]

    return frentes[0], historial