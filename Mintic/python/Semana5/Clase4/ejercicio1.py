# de la matriz se cogen las diagonal inferiores, una si y otra no, de tal
# forma que se tienen 3 diagonales y se calcula max y min

import numpy as np

matrizEjemplo = np.array([[10, -234, 345, -90, 19], 
        [20, 36, -90, -32, 45], 
        [56, 13, 17, 65, 23], 
        [-14, -23, 35, 23, 21], 
        [-500, -32, 86, 32, 50]])


#forma 1
#arrayAuxiliar = []
# for index, data in np.ndenumerate(matrizEjemplo):
#     i = index[0]
#     j = index[j]
#     if i+j >=4 and (i+j) % 2 ==0: 
#         arrayAuxiliar.append(data)
#         print(index, data)

# print(arrayAuxiliar)
# print("el máximo de los valores señalados es ", max(arrayAuxiliar))
# print("el mínimo de los valores señalados es ", min(arrayAuxiliar))

# forma 2
maximo = matrizEjemplo.min()
posicionMax = (0, 0)
minimo = matrizEjemplo.max()
posicionMin = (0, 0)
for index, data in np.ndenumerate(matrizEjemplo):
    i = index[0]
    j = index[1]
    if i+j >= 4 and (i+j) % 2 == 0:
        if data >= maximo:
            maximo = data
            posicionMax = index
        if data <= minimo:
            minimo = data
            posicionMin = index


print(maximo, posicionMax)
print(minimo, posicionMin)