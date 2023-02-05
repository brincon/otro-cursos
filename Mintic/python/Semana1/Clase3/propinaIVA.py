#Paso 1: pedir el total de la factura
totalFactura = int(input("por favor ingrese el valor total de la factura: "))
#Paso 2: pedir el porcentaje de propina que se quiere entregar
porcentajePropina = int(input("Por favor ingrese el valor que quiere dar de propina: "))
#Paso 3: Calcular el valor del IVA del 19%
valorIVA = totalFactura * 0.19
#Paso 4: Calcular el subtotal (total de la factura - valor del iva)
subtotal = totalFactura - valorIVA
#Paso 5: Calcular el valor de la propina (subtotal * propina/100)
valorPropina = subtotal * porcentajePropina / 100
#Paso 6: Mostrar el resultado
print (f"El valor total de la factura fue {totalFactura}")
print (f"El valor del IVA fue {valorIVA}")
print (f"El valor del subtotal fue {subtotal}")
print (f"El valor de la propia fue {valorPropina}")
print (f"El valor total de la compra más propina es ${totalFactura + valorPropina} pesos")

