"""1. Una empresa quiere saber cuanto gasta en total en Bono de Locomocion y
Alimentacion de todos sus trabajadores. Se sabe que la empresa tiene un total 
de n trabajadores y cada uno tiene distinto sueldo, sin embargo a todos se les paga los
mismos porcentajes de locomocion y movilizacion calculados de acuerdo con el sueldo de cada uno. 
El bono de Locomocion es un 14% (14/100). del sueldo y el bono de Alimentacion es un 9% (9/100)
del sueldo.

Usted debe realizar un Algoritmo que permita por cada uno de los n trabajadores:

Insgresar el Ci de cada Trabajador (es un entero)
Ingresar el sueldo de cada uno, el que no puede ser menor de 5000bs, sino se cumple esa condicion
debe volver a ingresarlo (Validar)
A medida que se ingrese se vaya calculando y mostrando cuando paga por cada trabajador en cada uno 
de los bonos(locomocion y alimentacion)
Finalmente, cuando se ingresen todos se indique cuanto la empresa gasta
. Se gasto en total XX por Conceptos de Locomocion
. Se gasto en total XX por Conceptos de Alimentacion"""

def validar(sueldo):
    if sueldo >= 5000: return True
    else: return False

def ingresar_ci():
    while True:
        try:
            ci = int(input("Ingrese el CI del trabajador: "))
            return ci
        except ValueError:
            print("CI invalido, por favor ingrese un numero entero.")

def ingresar_sueldo():
    while True:
        try:
            sueldo = int(input("Ingrese el sueldo del trabajador: "))
            if validar(sueldo):
                return sueldo
            else: print("Sueldo invalido, el sueldo debe ser mayor o igual a 5000bs.")
        except ValueError:
            print("Sueldo invalido, por favor ingrese un numero entero.")

def mostrar():
    print("Ingrese la cantidad de Trabajadores: ")
    n = int(input())
    total_locomocion = 0
    total_alimentacion = 0
    for i in range(n):
        print(f"\n --- Trabajador {i+1} ---")
        ci = ingresar_ci()
        sueldo = ingresar_sueldo()
        bono_locomocion = sueldo * 0.14
        bono_alimentacion = sueldo * 0.09
        total_locomocion += bono_locomocion
        total_alimentacion += bono_alimentacion
        print(f"Bono de Locomocion para el trabajador {ci}: {bono_locomocion:.2f} bs.")
        print(f"Bono de Alimentacion para el trabajador {ci}: {bono_alimentacion:.2f} bs.")
    print(f"\n--- Total Gastado por Concepto de Locomocion: {total_locomocion:.2f} bs.")
    print(f"--- Total Gastado por Concepto de Alimentacion: {total_alimentacion:.2f} bs.")
mostrar()
