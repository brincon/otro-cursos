# mbox-short.txt
fname = input("Enter file name: ")
try: 
    fh = open(fname)
except:
    print("El archivo no se puede abrir", fname)
    exit()

counts = dict()
for line in fh:
    line = line.rstrip()
    palabras = line.split()
    if len(palabras) < 1: continue
    if palabras[0] != "From": continue 
    correo = palabras[1] # segunda palabra, es decir el correo
    counts[correo] = counts.get(correo,0) + 1
    ## otra forma
    #if correo not in counts :  #si la segunda palabra no esta en la lista es igual a 1, de lo contrario sera el valor anterior más 1
        #counts[correo]= 1
    #else:
        #counts[correo]= counts[correo] + 1
print (counts)
#mayor = None
#for valor in counts:
#    if mayor is None or counts[valor] > mayor:
#        mayor = counts[valor]
#print('Mayor:', mayor)

clavemayor= None
mayor = None
for clave,val in counts.items():
    if mayor is None or val > mayor:
        clavemayor = clave
        mayor = val
print(clavemayor, mayor)

# Dado que python puede iterar a través de dos variables se puede hacer se convierte a items el diccionario, 
# esto lo que hace es armar tuplas dentro de una lista. las listas son [], los diccionarios están en llaves {}
