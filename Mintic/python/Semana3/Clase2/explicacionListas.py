#definiendo una lista
myList = [1, 34, 52, 87, -25, 90]
          #0  #1  #2  #3  #4  #5

#imrpimir un elemento especifico a través de su índice
print(myList[2])

#modificar un elemento especifico a través de su índice
myList[4] = -23

#leer un elemento de derecha a izquierda con indices negativos
print(myList[-1])#acceder al primer elemento de deerecha a izquierda 

#imprimir la lista completa
print (myList)

#agregar un dato al final de la lista
myList.append(120)
#imprimir el dato recientemente agregado
print (myList[6])

#imprimir la lista mostrando el nuevo dato
print(myList)

#eliminar un valor de una lista
myList.remove(34)
print(myList)

#agregar un valor a una lista en la posición que quiera
myList.insert(3, -500)
print(myList)

#eliminar datos de uan lista por su indice
del myList[4]
print(myList)

#eliminar y obtener el último elemento de la lista
elementoEliminado = myList.pop()
print(elementoEliminado)
print(myList)

#conocer cuantos elementos tiene una lista
print(f"La lista tiene {len(myList)} elementos")

#sumar elementos de una lista
print(f"la suma de los elementos de la lista es {sum(myList)}")

#identificar si un elemento hace parte de una lista
print (1 in myList)
print (-3443 in myList)

#ordenar una lista de manera ascendente
myList.sort()
print(myList)

#ordenar una lista de manera descendente
myList.reverse()
print(myList)

#calcular el máximo de una lista
print(max(myList))

#calcular el mínimo de una lista
print(min(myList))

namelist = ["Daniel", "Ana", "Carlos", "Jose"]
namelist.sort()
print("lista de nombres ordenada:", namelist)