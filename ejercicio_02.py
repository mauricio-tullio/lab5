"""
EJERCICIO 02: Validación de contraseña segura

Implementa una función que reciba una contraseña y verifique: 
    1. Que tenga al menos 8 caracteres de longitud.
    2. Que contenga al menos un número (puedes usar un bucle o una verificación con dígitos).
    3. Que contenga al menos una letra mayúscula.

La función debe retornar True si cumple todas las condiciones, y False en caso contrario. 
(Ayuda: puedes crear funciones auxiliares pequeñas para cada validación, fomentando la modularidad de tu programa).

Ejemplos de casos de prueba:
    - es_contrasena_segura("Python123") -> True
    - es_contrasena_segura("clave") -> False
    - es_contrasena_segura("12345678") -> False
"""

def largo_contraseña(contraseña):
    if len(contraseña) >= 8:
        return True
    return False


def numero_contraseña(contraseña):
    for i in contraseña:
        if i.isdigit():
            return True
    return False
        
def letra_contraseña(contraseña):
    for i in contraseña:
        if i.isupper():
            return True
    return False
        
def comprobacion_contraseña(contraseña):
    if(largo_contraseña(contraseña) and numero_contraseña(contraseña) and letra_contraseña(contraseña)):
        return True
    else:
        return False


if(comprobacion_contraseña("clave")):
    print("Segura")
else:
    print("Insegura")
