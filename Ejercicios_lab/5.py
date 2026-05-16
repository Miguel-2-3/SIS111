"""2. Obtenga la suma de numeros primos comprendidos entre 2...n
Un numero primo es aquel número natural mayor que 1 que solo tiene dos divisores: el 1 y él mismo.
Si intentas dividirlo por cualquier otro número, el resultado no es entero."""
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
def ingresar_n():
    while True:
        try:
            n = int(input("Ingrese un numero  entero mayor o igual a 2: "))
            if n >= 2:
                return n
            else:
                print("Numero invalido, ingrese un numero entero mayor o igual a 2.")
        except ValueError:
            print("Numero invalido, ingrese un numero entero.")
def mostrar():
    n = ingresar_n()
    suma_primos = 0
    lista_primos = ""
    for i in range(2, n + 1):
        if primo(i):
            suma_primos += i
            lista_primos += str(i) + ", "
    print(f"Numeros primos: {lista_primos}")
    print(f"La suma de los numeros primos es: {suma_primos}")
mostrar()