import time
import numpy as np

def medir_tiempo(func):
    """
    Mide el tiempo de ejecución de una función.

    Parámetros:
        func (function): Función a evaluar.

    Retorna:
        tuple:
            - resultado de la función
            - tiempo de ejecución en segundos
    """
    inicio = time.time()
    resultado = func()
    fin = time.time()
    return resultado, fin - inicio

def desviacion_estandar(valores):
    """
    Calcula la desviación estándar de un conjunto de valores.

    Esta métrica permite evaluar la estabilidad y robustez del algoritmo
    a través de múltiples ejecuciones.

    Parámetros:
        valores (list): Lista de valores numéricos.

    Retorna:
        float: Desviación estándar.
    """
    return np.std(valores)


def promedio(valores):
    """
    Calcula el promedio de un conjunto de valores.

    Parámetros:
        valores (list): Lista de valores numéricos.

    Retorna:
        float: Valor promedio.
    """
    return np.mean(valores)