def mayormenor(a,b,c)
    if(a>b and a>c):
        return f"Mayor: a: {a}"
    elif(b>a and b>c):
        return f"Mayor: b: {b}"
    else:    return f"Mayor: c: {c}"
print("**********Mayor Menor**********")
print("Introduzca el valor de a: ")
a= int(input())
print("Introduzca el valor de b: ")
b= int(input())
print("Introduzca el valor de c: ")
c= int(input())
print(mayormenor(a,b,c))