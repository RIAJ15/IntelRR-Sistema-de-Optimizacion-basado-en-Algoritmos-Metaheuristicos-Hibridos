def domina(a, b):
    """
    Verifica si la solución a domina a b
    """
    return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))


def clasificar_pareto(poblacion):
    """
    Clasifica soluciones en frentes de Pareto
    """
    frentes = []
    poblacion_restante = poblacion[:]

    while poblacion_restante:
        frente = []
        for p in poblacion_restante:
            if not any(domina(q['fitness'], p['fitness']) for q in poblacion_restante):
                frente.append(p)

        frentes.append(frente)
        poblacion_restante = [p for p in poblacion_restante if p not in frente]

    return frentes