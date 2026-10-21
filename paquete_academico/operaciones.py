"""calcular_promedio(lista_notas): Retorna el promedio de una lista de números.
    encontrar_maximo(lista_notas): Retorna la nota más alta de una lista de números"""

def calcular_promedio(lista_notas):
    if not lista_notas:
        return 0
    return sum(lista_notas) / len(lista_notas)

def encontrar_maximo(lista_notas):
    if not lista_notas:
        return None
    return max(lista_notas)