def ingresarDatos():
    
    n = int(input("Ingrese el número de asignaturas: "))
    datos = []
    for i in range(n):
        print("Asignatura", i + 1)
        nombre = input("Nombre de la asignatura: ")
        num_ex = int(input("Número de exámenes: "))
        examenes = []
        for j in range(num_ex):
            nota = float(input("Nota examen: "))
            examenes.append(nota)
        num_pr = int(input("Número de prácticas: "))
        practicas = []
        for j in range(num_pr):
            nota = float(input("Nota práctica: "))
            practicas.append(nota)
        porc_examen = float(input("Porcentaje de exámenes(%): "))
        porc_practicas = float(input("Porcentaje de prácticas(%): "))
        datos.append({"nombre": nombre,"examenes": examenes,"practicas": practicas,
                     "porc_examen": porc_examen,"porc_practicas": porc_practicas
        })
    return datos

def calcular():
    datos = ingresarDatos()
    promedios = []
    for dato in datos:
        prom_examen = sum(dato.get("examenes")) / len(dato.get("examenes"))
        prom_practicas = sum(dato.get("practicas")) / len(dato.get("practicas"))
        promedio_general = (prom_examen * dato.get("porc_examen") / 100) + (prom_practicas * dato.get("porc_practicas") / 100)
        promedios.append({"nombre": dato.get("nombre"),"promedio": promedio_general
        })
    return promedios

def mostrar():
    promedios = calcular()
    for promedio in promedios:
        print("El promedio de", promedio.get("nombre"), "es:", promedio.get("promedio"))
mostrar()