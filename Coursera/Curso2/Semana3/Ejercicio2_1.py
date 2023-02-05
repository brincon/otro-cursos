# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
contador = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    contador = contador + 1
    line = line.rstrip()  
    lin = line[20:]
    li = float (lin)
    total = total + li
print ("Average spam confidence:", total/contador)

# se debe evitar usar suma como variable ya que hay una función llamada así
