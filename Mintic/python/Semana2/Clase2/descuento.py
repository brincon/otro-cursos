# ejercicio 3:  preguntar el total de una compra. si el valor es mauor a 100000, dar un descuento del 10%
# ejercicio 3
compra = float(input("Por favor ingrese el valor de su compra: "))

if compra > 100000:
    descuento = compra * 10/100
    print(f"El valor del descuento es {descuento}")
else:
    descuento = 0

total = compra - descuento
print(f"El total de su compra es {total}")