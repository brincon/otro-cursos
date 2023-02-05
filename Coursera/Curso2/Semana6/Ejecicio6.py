# mbox-short.txt
# corresponde al primer ejercicio del capitulo de tuplas
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

#print (counts)

lis = list()                         #crea una lista para agregar el diccionario dentro de ella
for key,val in counts.items():       #como el diccionario tiene dos valores se crean tuplas o items para que itera a través de los dos
    nuevatupla = (val,key)           #se le cambia el orden a la tupla
    lis.append(nuevatupla)          #y despues si se agrega a la lista

lis = sorted(lis, reverse=True)     #se ordena la lista en orden descendente

for val,key in lis[:1]:              #se pone a iterar a través de la palabra más común y se imprime
    print (val, key)




