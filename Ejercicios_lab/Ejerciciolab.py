def validar(estado):
    if estado == 1: return True
    elif estado == 2: return True
    elif estado == 3: return True
    else: return False
def mostrar():
    print("Ingrese la cantidad de Trabajadoras: ")
    n = int(input())
    bono_por_hijo = 2000

    solteras = 0
    casadas = 0
    pareja = 0
    hijos_solteras = 0
    hijos_casadas = 0
    hijos_pareja = 0
    for i in range(n):
        print(f"Trabajadora {i+1}:")
        print("Ingrese el Estado Civil:")
        print("1: Soltera")
        print("2: Casada")
        print("3: En pareja")

        estado = int(input())
        while validar(estado) == False:
            print("Estado invalido")
            print("Ingrese un estado civil valido: ")
            estado = int(input())
        
        print("Ingrese la cantidad de hijos: ")
        hijos = int(input())
        if estado == 1:
            solteras += 1
            hijos_solteras += hijos
        elif estado == 2:
            casadas += 1
            hijos_casadas += hijos
        elif estado == 3:
            pareja += 1
            hijos_pareja += hijos
    total_hijos = hijos_solteras + hijos_casadas + hijos_pareja
    total_bono = total_hijos * bono_por_hijo
    print(f"Hay {solteras} trabajadoras Solteras, con {hijos_solteras} hijos")
    print(f"Hay {casadas} trabajadoras Casadas, con {hijos_casadas} hijos")
    print(f"Hay {pareja} trabajadoras en Pareja, con {hijos_pareja} hijos")
    print(f"El total del bono entregado por la empresa es de {total_bono} bs.")

mostrar()


