import numpy as np

matrizEjemplo = np.array([[10, -234, 345, -90, 19], 
        [20, 36, -90, -32, 45], 
        [56, 13, 17, 65, 23], 
        [-14, -23, 35, 23, 21], 
        [-500, -32, 86, 32, 50]])

print(matrizEjemplo)
#sacar una suma de los elementos para cada fila
print("suma elementos de cada fila")
print(matrizEjemplo.sum(axis=1))

#sacar una suma de los elementos para cada columna
print("suma elementos de cada columna")
print(matrizEjemplo.sum(axis=0))

#cacar el máximo de cada fila
print("máximo de cada fila")
print(matrizEjemplo.max(axis=1))
#cacar el máximo de cada columna
print("máximo de cada columna")
print(matrizEjemplo.max(axis=0))

#cacar el minimo de cada fila
print("mínimo de cada fila")
print(matrizEjemplo.min(axis=1))
#cacar el minimo de cada columna
print("mínimo de cada columna")
print(matrizEjemplo.min(axis=0))

#Calcular la matriz triangular superior:
triangularSuperior = np.triu(matrizEjemplo)
print("triangular superior")
print(triangularSuperior)

#Calcular la matriz triangular inferior:
triangularInferior = np.tril(matrizEjemplo)
print("triangular inferior")
print(triangularInferior)

#calcular la transpuesta de una matriz
print("Matriz:")
print(matrizEjemplo)
transpuesta = np.transpose(matrizEjemplo)
print("Transpuesta:")
print(transpuesta)


