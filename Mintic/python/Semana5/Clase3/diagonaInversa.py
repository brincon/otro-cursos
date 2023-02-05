import numpy as np

matrizEjemplo = np.array([[10, -234, 345, -90, 19], 
        [20, 36, -90, -32, 45], 
        [56, 13, 17, 65, 23], 
        [-14, -23, 35, 23, 21], 
        [-500, -32, 86, 32, 50]])


tamanoMatriz = matrizEjemplo.shape
print("tamaño", tamanoMatriz)

diagonaInversa = []

for index, data in np.ndenumerate(matrizEjemplo):
    #print(index, data)
    if index[1] == (tamanoMatriz[1] - index[0] -1):
        diagonaInversa.append(data)
        
print(diagonaInversa)
   