def funciones():
    while True:
            print("\n1. Consultar saldo")
            print("\n2. Depositar dinero")
            print("\n3. Retirar dinero")
            print("\n4. Salir")
            
            opcion = input("Elija una opción: ")
    
            match opcion:
                case "1":
                    print(f"Su saldo actual es: ${saldo}")
                case "2":
                    monto = float(input("Ingrese monto a depositar: "))
                    if monto > 0:
                        saldo += monto
                        print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
                    else:
                        print("Monto inválido.")
                case "3":
                    monto = float(input("Ingrese monto a retirar: "))
                    if 0 < monto <= saldo:
                        saldo -= monto
                        print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
                    elif monto > saldo:
                        print("Fondos insuficientes")
                    else:
                        print("Monto inválido")
                case "4":
                    print("Gracias por usar el cajero.")
                    break
                case _:
                    print("Opción inválida.")