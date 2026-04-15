def evaluar_ruta(ruta, distancia, costo, tiempo):
    """
    Evalúa una ruta en términos de distancia, costo y tiempo.

    Parámetros:
        ruta (list): orden de ciudades
        distancia (matrix)
        costo (matrix)
        tiempo (matrix)

    Retorna:
        tuple: (distancia_total, costo_total, tiempo_total)
    """

    dist_total = 0
    costo_total = 0
    tiempo_total = 0

    for i in range(len(ruta) - 1):
        a = ruta[i]
        b = ruta[i + 1]

        dist_total += distancia[a][b]
        costo_total += costo[a][b]
        tiempo_total += tiempo[a][b]

    return dist_total, costo_total, tiempo_total