"""1. Introduzca dos numeros que tengan mas de 3 digitos y determine si son o no AMIGOS. (Validar)
(un numero es amigo del otro cuando la suma de sus digitos es igual a la suma de los digitos del otro
numero)"""
def validar(numero):
    if numero >= 1000:
        return True
    else:
        return False
def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma
def ingresar_numero():
    while True:
        try:
            numero = int(input("Ingrese un numero con mas de 3 digitos: "))
            if validar(numero):
                return numero
            else:
                print("Numero invalido, ingrese un numero con mas de 3 digitos.")
        except ValueError:
            print("Numero invalido, ingrese un numero entero.")
def mostrar():
    print("Ingrese el primer numero: ")
    numero1 = ingresar_numero()
    print("Ingrese el segundo numero: ")
    numero2 = ingresar_numero()
    suma1 = suma_digitos(numero1)
    suma2 = suma_digitos(numero2)
    if suma1 == suma2:
        print(f"Los numeros {numero1} y {numero2} Son Amigos.")
    else:
        print(f"Los numeros {numero1} y {numero2} No Son Amigos.")
mostrar()