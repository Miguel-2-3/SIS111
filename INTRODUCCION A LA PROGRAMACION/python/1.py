num1= float(input("INTRODUCE EL PRIMER NUMERO"))
num2= float(input("INTRODUCE EL SEGUNDO NUMERO"))
OP = input("INTRODUCE LA OPERACION QUE DESEAS REALIZAR: +, -, *,/")
if OP == "+":
    print(num1+num2)
elif OP == "-": 
    print(num1-num2)
elif OP == "*": 
    print(num1*num2)
elif OP == "/": 
    print(num1/num2)
else:
    print("OPERACION NO VALIDA")