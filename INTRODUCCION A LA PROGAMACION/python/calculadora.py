def calculadora(num1, num2, operacion):
    if (operacion == "+"):
        return num1 + num2
    if (operacion == "-"):
        return num1 - num2
    if (operacion == "*"):
        return num1 * num2
    if (operacion == "/"):
        if(num2 !=0):
            return num1/num2
        else: return f"NO SE PUEDE DIVIDIR ENTRE {num2}"
    else: return "ERROR"
print("Calculadora SIS-111")
print("*******************")
print("INTRODUZCA EL PRIMER NUMERO")
num1 = float(input())
print("introduzca el operador basico(+, -, *, /)")
operador = input()
print("INTRODUZCA EL SEGUNDO NUMERO")
num2 = float(input())
print("RESULTADO:")
print(calculadora(num1, num2, operador))
print("GRACIAS POR USAR LA CALCULADORA")

