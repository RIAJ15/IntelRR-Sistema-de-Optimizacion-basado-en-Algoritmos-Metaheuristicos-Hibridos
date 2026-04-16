import time
import numpy as np

def medir_tiempo(func):
    inicio = time.time()
    resultado = func()
    fin = time.time()
    return resultado, fin - inicio


def desviacion_estandar(valores):
    return np.std(valores)


def promedio(valores):
    return np.mean(valores)