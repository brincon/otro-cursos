fname = input("Enter file name: ")
fh = open(fname)
for linea in fh:
    linea = linea.upper()
# Cambiar las lineas a mayuscula
    linea = linea.rstrip()
    # Quita los espacios a la derecha
    print(linea)

# otra opción
#fname = input("Enter file name: ")
#fh = open(fname)
#for linea in fh:
    #linea = linea.rstrip()
# Quita los espacios a la derecha
    #print(linea.upper())
# Se imprime y al mismo tiempo se pide que pase todo a mayuscula