from data.ciudades import *
from algorithms.nsga2 import nsga2
from algorithms.hybrid import modelo_hibrido
from utils.metrics import desviacion_estandar
from visualization.dashboard import Dashboard
import time

# Datos
ciudades = generar_ciudades(10)
distancia = calcular_distancia(ciudades)
costo, tiempo_m = generar_costo_tiempo(10)

# NSGA-II
inicio = time.time()
frente_nsga, hist_nsga = nsga2(10, distancia, costo, tiempo_m)
t_nsga = time.time() - inicio

# Híbrido
inicio = time.time()
frente_h, hist_h = modelo_hibrido(10, distancia, costo, tiempo_m)
t_h = time.time() - inicio

print("Tiempo NSGA:", t_nsga)
print("Tiempo Híbrido:", t_h)

# Desviación
vals = []
for _ in range(5):
    f, _ = modelo_hibrido(10, distancia, costo, tiempo_m)
    vals.append(min(sum(x["fitness"]) for x in f))

print("Desviación:", desviacion_estandar(vals))

# Dashboard
Dashboard(hist_nsga, hist_h, [r["fitness"] for r in frente_h])