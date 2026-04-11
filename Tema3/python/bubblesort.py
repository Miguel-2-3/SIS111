def bubblesort(lista, ascendente=True):
   cantidad = len(lista)
   for i in range(cantidad - 1):
       for j in range(cantidad-i-1):
          #aux = 0
            if(ascendente):
                if lista[j] > lista[j+1]:
                    lista[j],lista[j+1] = lista[j+1],lista[j]
                    #Con manejo de auxiliares#
                    #aux = lista[j]
                    #lista[j] = lista[j+1]
                    #lista[j+1] = aux
                else: 
                    if lista[j] < lista[j+1]:
                        lista[j],lista[j+1] = lista[j+1],lista[j]
   return lista

lista = [7, 12, 9, 11, 3]

print(bubblesort(lista, True))
print(bubblesort(lista, False))