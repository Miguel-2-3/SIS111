import random
def aleatorios(n):
    pares = []
    impares = []
    for i in range(n):
        numero = random.randint(1,100)
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    sumapares = sum(pares)
    sumaimpares = sum(impares)
    return pares, impares, sumapares, sumaimpares

print("*********Lista de aleatorios pares e impares*********")
n = int(input("Introduzca el valor de n: "))
pares, impares, sumapares, sumaimpares = aleatorios(n)
print("Lista de pares:", pares)
print("Lista de impares:", impares)
print("Suma de pares:", sumapares)
print("Suma de impares:", sumaimpares)