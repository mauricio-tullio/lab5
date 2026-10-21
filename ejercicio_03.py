"""
EJERCICIO 03: Día del año.

1. Haga una función que dado un mes (en número), retorne la cantidad de días que tiene el mes (considere febrero con 28 días)
2. Haga otra función que dado un mes y el día actual del mes (ambos en número), calcule la cantidad de días que van del año
3. Pídale al usuario que ingrese el mes actual (en número). Debe validar el dato ingresado.
4. Pídale al usuario que ingrese el día actual (en número). Debe validar el dato ingresado y debe tener coherencia con el mes
   indicado en el paso anterior. Por ejemplo, abril no puede tener 31 días.
5. Calcule el día presente del año según los datos ingresados por el usuario, utilizando las funciones que acaba de implementar
6. Muestre en pantalla el resultado

"""
def cantidad_dias_mes(mes):
    if mes == 2:
        return 28
    elif mes in (4,6,9,11):
        return 30
    else:
        return 31
    
def cantidad_dias(dia, mes):
      total = 0
      for i in range(1,mes):
          total += cantidad_dias_mes(i)
      return total + dia

while True:
    try:

      dia = int(input("Ingresa el dia: ")) 
      mes = int(input("Ingresa el mes: "))

      if (0 < dia <= 31) and (0 < mes <= 12):
          break
      else: print("Ingrese valores validos")
      
    except ValueError:
        print("Ingrese un numero valido")

print(cantidad_dias(dia,mes))