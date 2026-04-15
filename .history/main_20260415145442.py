from data.ciudades import generar_ciudades, calcular_distancia, generar_costo_tiempo
from algorithms.hybrid import modelo_hibrido
from algorithms.nsga2 import nsga2
from visualization.plots import graficar_convergencia, graficar_pareto, comparar_convergencia
from utils.metrics import desviacion_estandar
from config import *
import time

# =========================
# GENERAR DATOS
# =========================
ciudades = generar_ciudades(NUM_CIUDADES)
distancia = calcular_distancia(ciudades)
costo, tiempo_m = generar_costo_tiempo(NUM_CIUDADES)

# =========================
# NSGA-II SOLO
# =========================
inicio = time.time()
frente_nsga, hist_nsga = nsga2(NUM_CIUDADES, distancia, costo, tiempo_m)
tiempo_nsga = time.time() - inicio

# =========================
# HÍBRIDO
# =========================
inicio = time.time()
frente_hibrido, hist_hibrido = modelo_hibrido(NUM_CIUDADES, distancia, costo, tiempo_m)
tiempo_hibrido = time.time() - inicio

# =========================
# RESULTADOS
# =========================
print("\n=== NSGA-II ===")
for r in frente_nsga:
    print(r["fitness"])

print("\n=== HÍBRIDO ===")
for r in frente_hibrido:
    print(r["fitness"])

# =========================
# MÉTRICAS
# =========================
print("\nTiempo NSGA-II:", tiempo_nsga)
print("Tiempo Híbrido:", tiempo_hibrido)

# Desviación estándar (5 ejecuciones)
resultados = []

for _ in range(5):
    frente, _ = modelo_hibrido(NUM_CIUDADES, distancia, costo, tiempo_m)
    mejores = [sum(r["fitness"]) for r in frente]
    resultados.append(min(mejores))

print("Desviación estándar:", desviacion_estandar(resultados))

# =========================
# GRÁFICAS
# =========================
graficar_convergencia(hist_hibrido)
comparar_convergencia(hist_nsga, hist_hibrido)
graficar_pareto([r["fitness"] for r in frente_hibrido])