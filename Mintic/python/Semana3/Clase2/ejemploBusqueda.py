# numerolos aleatorios

import random

#print(random.random())

#numeros aleatorios en un rango de enteros
#print(random.randint(1,10))

# agregar 10 números aleatorios a una lista
listOfRandomNumbers = []
for randomNumber in range(0,10):
    listOfRandomNumbers.append(random.randint(1,100))

#print(listOfRandomNumbers)

# Función que reciba un número n y devuelva una lista con N numeros
# aleatorios entre 0 y 100

def aleatorio(N, inferiorRange, superiorRange):
    lis = []
    for numero in range (0, N):
        lis.append(random.randint(inferiorRange, superiorRange))
    return lis

#print(aleatorio(10, 5, 10))

# Buscar si un número x está en la lista de aleatorios.
# En caso de que el número este devolver la posición del número.

def searchNumberInRandomList(numberToFind, listToSearch):
    found = False
    for index, element in enumerate(listToSearch):
        if element == numberToFind:
            print("encontré el elemento", numberToFind)
            return index
    return found

randomList = aleatorio(50, 0, 100)
found = searchNumberInRandomList(19, randomList)
print(randomList)
print(found)






