# precio base de los huevos = 1800
# precio base de los huevos = 5000
# si alguien compra más de 10 canastas, el precio 1000
# si alguien compra más de 10 canastas de huevos y además compra más de 10 paquetes de arepas
# el precio de los huevos es 800 y el de las arepas es 2000

#paso1: preguntar cuántos huevos quiere comprar la personas
cantidadHuevos = int(input("Digite la cantidad de canastas de huevos que quiere comprar: "))
#paso2: preguntar si la persona quiere comprar arepas
quiereArepas = input("¿usted desea llevar arepas? ").lower()
#paso3: si la persona quiere comprar arepas, preguntarle cuantos
cantidadArepas = 0
if quiereArepas == "si" or quiereArepas == "sí":
    cantidadArepas = int(input("Digite la cantidad de arepas que quiere comprar: "))

#paso4: calcular el total de la compra
if cantidadArepas > 10 and cantidadHuevos > 10:
    precioHuevos = 800
    precioArepas = 2000
elif cantidadHuevos > 10:
    precioHuevos = 1000
    precioArepas = 5000
else:
    precioHuevos = 1800
    precioArepas = 5000

subtotal = precioHuevos * cantidadHuevos + precioArepas * cantidadArepas

#condiones adicionales que se deben cumplir
#1. si el total de la compra es mayor a 50 mil, y solo estoy comprando un producto, dar un descuento adicional del 10%
#2. si el total de la compra es mayor a 50 mil y además se estan comprando huevos y arepas, el descuentos es del 15%
#3. mostrarle al usuario el ttoal de la compra y también el total del descuento

#mi forma (me faltó que imprima cuando no tiene descuento)
#if totalCompra > 50000:
#    if cantidadHuevos > 0 and cantidadArepas > 0:
#        descuento = totalCompra * 0.15
#        totalCompra = totalCompra - descuento
#        print ("El total de su descuento es ${descuento} pesos")
#    else:
#        descuento = totalCompra * 0.10
#        totalCompra = totalCompra - descuento
#        print (f"El total de su descuento es ${descuento} pesos")

#print (f"El total de su compra es ${totalCompra} pesos")

#opción1 profe
if subtotal > 50000 and (cantidadHuevos == 0 or cantidadArepas == 0):
    descuento = subtotal * 10/100
    totalFinal = subtotal - descuento
elif subtotal > 50000 and (cantidadHuevos > 0 and cantidadArepas > 0):
    descuento = subtotal * 15/100
    totalFinal = subtotal - descuento
else:
    descuento = 0
    totalFinal = subtotal

print (f"El descuento de la compra es de ${descuento} pesos")
print (f"El total de la compra es de ${totalFinal} pesos")

#opción2 con if anidado

descuento = 0
if subtotal > 50000:
    if cantidadHuevos == 0 or cantidadArepas == 0:
        descuento = 10/100
    else:
        descuento = subtotal * 15/100

total = subtotal - descuento





