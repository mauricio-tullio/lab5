"""En reportes.py, define la función:
    generar_resumen(lista_notas): Utiliza las funciones de operaciones.py para imprimir un reporte en consola con 
    el promedio y la nota máxima."""

from paquete_academico import operaciones

def reporte(lista):
    print(f"El promedio es {operaciones.calcular_promedio(lista)}")
    print(f"El valor maximo es {operaciones.encontrar_maximo(lista)}")