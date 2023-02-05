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
    hora = palabras[5] # quinta palabra, es decir la hora
    nuevhora = hora.split(":")
    nuevahora = nuevhora[0]
    counts[nuevahora] = counts.get(nuevahora,0) + 1

lis = list()
for key,val in counts.items():
    nuevatupla = (key, val)
    lis.append(nuevatupla)

lis = sorted(lis)

for key,val in lis: 
    print(key, val)