"""2.Una persona se va de compras a la tienda "El diablo" decide llevar un control 
sobre lo que va comprando, para saber la cantidad de dinero que tendrá que pagar al 
llegar a la caja. La tienda tiene una promoción del 20% (20/100) de descuento sobre 
aquellos artículos cuya etiqueta tenga el número 666. Todos los artículos tienen etiqueta. 
La persona comprará exactamente n productos.
Usted debe realizar un Algoritmo que permita ingresar:

El valor de cada producto El número que aparece en la etiqueta. Estos números son entre 1 y 1000, 
no se permite ingresar otro número fuera de este rango (Validar)

Recuerde que, el algoritmo debe aplicar el descuento al valor del producto cuando corresponda 
(los que tienen etiqueta 666)

Finalmente debe mostrar el total final de dinero que esta persona deberá pagar por el total 
de todos sus productos."""

def validar(etiqueta):
    if etiqueta >= 1 and etiqueta <= 1000: 
        return True
    else: 
        return False

def ingresar_etiqueta():
    while True:
        try:
            etiqueta = int(input("Ingrese el numero de la etiqueta del producto: "))
            if validar(etiqueta):
                return etiqueta
            else: print("Numero de etiqueta invalido, ingrese un numero entre 1 y 1000.")
        except ValueError:
            print("Numero de etiqueta invalido, ingrese un numero entero.")

def ingresar_precio():
    while True:
        try:
            precio = float(input("Ingrese el valor del producto: "))
            if precio >= 0:
                return precio
            else: print("Precio invalido, ingrese un precio mayor a 0.")
        except ValueError:
            print("Precio invalido, ingrese un precio valido.")

def mostrar():
    print("Ingrese la cantidad de productos que va a comprar: ")
    n = int(input())
    total = 0
    for i in range(n):
        print(f"\n--- Producto {i+1} ---")
        etiqueta = ingresar_etiqueta()
        precio = ingresar_precio()
        if etiqueta == 666:
            descuento = precio * 0.20
            precio_final = precio - descuento
            print(f"El producto tiene un descuento de 20%, el precio final es: {precio_final:.2f} bs.")
        else:
            precio_final = precio
            print(f"El producto no tiene descuento, el precio es: {precio_final:.2f} bs.")
        total += precio_final
    print(f"\n--- El total a pagar por los productos es: {total:.2f} bs. ---")
mostrar()