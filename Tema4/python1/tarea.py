salir = False

while salir == False:
    print("\n--- MENÚ ---")
    print("1. Sumar números")
    print("2. Restar números")
    print("3. Multiplicar números")
    print("4. Dividir números")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Programa finalizado")
        salir = True

    elif opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
        
        cantidad = int(input("¿Cuántos números vas a ingresar?: "))
        numeros = []

        for i in range(cantidad):
            num = float(input("Ingrese número: "))
            numeros.append(num)

        if opcion == "1":
            resultado = 0
            for n in numeros:
                resultado = resultado + n
            print("Resultado:", resultado)

        elif opcion == "2":
            resultado = numeros[0]
            for i in range(1, cantidad):
                resultado = resultado - numeros[i]
            print("Resultado:", resultado)

        elif opcion == "3":
            resultado = 1
            for n in numeros:
                resultado = resultado * n
            print("Resultado:", resultado)

        elif opcion == "4":
            resultado = numeros[0]
            error = False

            for i in range(1, cantidad):
                if numeros[i] == 0:
                    print("Error: no se puede dividir entre cero")
                    error = True
                else:
                    resultado = resultado / numeros[i]

            if error == False:
                print("Resultado:", resultado)

    else:
        print("Error: opción inválida")