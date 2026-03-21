def mayormenor(a,b,c):
    if(a>b and a>c):
        if(b>c):
            return f"Mayor: a: {a}  Menor: c: {c}"
        else:
            return f"Mayor: a: {a}  Menor: b: {b}"
    elif(b>a and b>c):
        if(a>c):
            return f"Mayor: b: {b}  Menor: c: {c}"
        else:
            return f"Mayor: b: {b}  Menor: a: {a}"
    else:
        if(a>b):
            return f"Mayor: c: {c}  Menor: b: {b}"
        else:
            return f"Mayor: c: {c}  Menor: a: {a}"


print("**********Mayor Menor**********")
print("Introduzca el valor de a: ")
a= int(input())
print("Introduzca el valor de b: ")
b= int(input())
print("Introduzca el valor de c: ")
c= int(input())
print(mayormenor(a,b,c))