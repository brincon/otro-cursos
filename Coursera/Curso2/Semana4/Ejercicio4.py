# romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    palabras = line.split()

    for palabra in palabras:
        if palabra in lst: 
            continue
        lst.append(palabra) 

lst.sort()   
print (lst)
# se pide agregar solo las palabras que no esten en la lista, primero se lee la linea, despues se divide en palabras
# y cada palabra se lee en otro bucle, si la palabra esta en la lista continue, es decir que no la agregue pero si no
# esta entonces agreguela a la lista.