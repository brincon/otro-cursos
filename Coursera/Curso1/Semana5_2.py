menor = None
mayor = None
while True :
    sval = input ('ingrese un numero : ')
    if sval == 'done' : 
        break
    try:
        fval = int(sval)
        if mayor is None or fval > mayor:
            mayor = fval
        if menor is None or fval < menor:
            menor = fval   
    except:
        print('Invalid input')
        continue

print ('Maximum is', mayor)
print ('Minimum is', menor)

