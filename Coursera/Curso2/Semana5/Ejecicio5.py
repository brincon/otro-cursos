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
    tercera = palabras[2]
    #print(palabras[2])
    if tercera not in counts :  #si la tercera palabra no esta en la lista es igual a 1, de lo contrario sera el valor anterior más 1
        counts[tercera]= 1
    else:
        counts[tercera]= counts[tercera] + 1

print (counts)
    


