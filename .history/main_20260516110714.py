from data.ciudades import generar_ciudades, calcular_distancia, generar_costo_tiempo
from algorithms.hybrid import modelo_hibrido
from algorithms.nsga2 import nsga2
from visualization.dashboard import Dashboard
from utils.metrics import desviacion_estandar, promedio
from config import *
import time


# ============================================================
# GENERACIÓN DE DATOS DEL PROBLEMA
# ============================================================

# Se generan las ciudades y matrices del problema
ciudades = generar_ciudades(NUM_CIUDADES)
distancia = calcular_distancia(ciudades)
costo, tiempo_m = generar_costo_tiempo(NUM_CIUDADES)


# ============================================================
# PRUEBA INDIVIDUAL PARA VISUALIZACIÓN
# ============================================================

# NSGA-II
inicio = time.time()
frente_nsga, hist_nsga = nsga2(NUM_CIUDADES, distancia, costo, tiempo_m)
tiempo_nsga = time.time() - inicio

# Modelo híbrido
inicio = time.time()
frente_hibrido, hist_hibrido = modelo_hibrido(NUM_CIUDADES, distancia, costo, tiempo_m)
tiempo_hibrido = time.time() - inicio


# ============================================================
# BENCHMARKING (PRUEBAS REPETIDAS)
# ============================================================

"""
Se ejecutan múltiples pruebas para obtener métricas más confiables
y evitar conclusiones basadas en una sola ejecución.
"""

NUM_PRUEBAS = 10

tiempos_nsga = []
tiempos_hibrido = []

fitness_nsga = []
fitness_hibrido = []

for _ in range(NUM_PRUEBAS):

    # -------------------------
    # NSGA-II
    # -------------------------
    inicio = time.time()
    frente, _ = nsga2(NUM_CIUDADES, distancia, costo, tiempo_m)
    tiempos_nsga.append(time.time() - inicio)

    mejor_nsga = min(sum(r["fitness"]) for r in frente)
    fitness_nsga.append(mejor_nsga)

    # -------------------------
    # HÍBRIDO
    # -------------------------
    inicio = time.time()
    frente, _ = modelo_hibrido(NUM_CIUDADES, distancia, costo, tiempo_m)
    tiempos_hibrido.append(time.time() - inicio)

    mejor_h = min(sum(r["fitness"]) for r in frente)
    fitness_hibrido.append(mejor_h)


# ============================================================
# RESULTADOS
# ============================================================

print("\n=== RESULTADOS NSGA-II ===")
for r in frente_nsga:
    print(r["fitness"])

print("\n=== RESULTADOS MODELO HÍBRIDO ===")
for r in frente_hibrido:
    print(r["fitness"])


# ============================================================
# MÉTRICAS DE RENDIMIENTO
# ============================================================

print("\n========== MÉTRICAS ==========")

print("Tiempo promedio NSGA-II:", promedio(tiempos_nsga))
print("Tiempo promedio Híbrido:", promedio(tiempos_hibrido))

print("Mejor fitness promedio NSGA-II:", promedio(fitness_nsga))
print("Mejor fitness promedio Híbrido:", promedio(fitness_hibrido))

print("Desviación estándar NSGA-II:", desviacion_estandar(fitness_nsga))
print("Desviación estándar Híbrido:", desviacion_estandar(fitness_hibrido))


# ============================================================
# DASHBOARD INTERACTIVO
# ============================================================

Dashboard(
    hist_nsga,
    hist_hibrido,
    frente_hibrido,
    ciudades
)