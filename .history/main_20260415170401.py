from data.ciudades import generar_ciudades, calcular_distancia, generar_costo_tiempo
from algorithms.hybrid import modelo_hibrido
from algorithms.nsga2 import nsga2
from visualization.plots import graficar_convergencia, graficar_pareto, comparar_convergencia
from utils.metrics import desviacion_estandar
from config import *
import time

# =========================
# GENERACIÓN DE DATOS
# =========================

# Genera un conjunto de ciudades con coordenadas aleatorias
ciudades = generar_ciudades(NUM_CIUDADES)

# Calcula la matriz de distancias entre ciudades
distancia = calcular_distancia(ciudades)

# Genera matrices simuladas de costo y tiempo
costo, tiempo_m = generar_costo_tiempo(NUM_CIUDADES)

# =========================
# EJECUCIÓN NSGA-II (BASELINE)
# =========================

# Medición del tiempo de ejecución del algoritmo NSGA-II
inicio = time.time()
frente_nsga, hist_nsga = nsga2(NUM_CIUDADES, distancia, costo, tiempo_m)
tiempo_nsga = time.time() - inicio

# =========================
# EJECUCIÓN MODELO HÍBRIDO (NSGA-II + PSO)
# =========================

# Medición del tiempo de ejecución del modelo híbrido
inicio = time.time()
frente_hibrido, hist_hibrido = modelo_hibrido(NUM_CIUDADES, distancia, costo, tiempo_m)
tiempo_hibrido = time.time() - inicio

# =========================
# IMPRESIÓN DE RESULTADOS
# =========================

print("\n=== RESULTADOS NSGA-II ===")
for r in frente_nsga:
    print(r["fitness"])

print("\n=== RESULTADOS MODELO HÍBRIDO ===")
for r in frente_hibrido:
    print(r["fitness"])

# =========================
# MÉTRICAS DE RENDIMIENTO
# =========================

# Tiempo de ejecución de cada algoritmo
print("\nTiempo NSGA-II:", tiempo_nsga)
print("Tiempo Híbrido:", tiempo_hibrido)

# Cálculo de desviación estándar para evaluar la robustez del modelo híbrido
resultados = []

for _ in range(5):
    frente, _ = modelo_hibrido(NUM_CIUDADES, distancia, costo, tiempo_m)
    
    # Se obtiene la mejor solución (mínima suma de objetivos)
    mejores = [sum(r["fitness"]) for r in frente]
    resultados.append(min(mejores))

print("Desviación estándar:", desviacion_estandar(resultados))

# =========================
# VISUALIZACIÓN DE RESULTADOS
# =========================

# Gráfica de convergencia del modelo híbrido
graficar_convergencia(hist_hibrido)

# Comparación entre NSGA-II y modelo híbrido
comparar_convergencia(hist_nsga, hist_hibrido)

# Visualización del frente de Pareto (distancia vs costo)
graficar_pareto([r["fitness"] for r in frente_hibrido])