#mbox-short.txt
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    palabras = line.rstrip()
    palabras = line.split()
    if len(palabras) < 1: continue
    if palabras [0] != "From": continue 

    print (palabras[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")