#pedirle al usuario dos valores númericos e imprimir el valor de ellos

valor1 = int(input("Por favor ingrese un número: "))
valor2 = int(input("Por favor ingrese un número: "))

if valor1 > valor2:
    mayor = valor1
else:
    mayor = valor2

print (f"El número mayor es: {mayor}")

# como lo hizo el profe
if valor1 > valor2:
    print ("El primer valor es mayor que el segundo")
elif valor1 < valor2:
    print ("El segundo valor es mayor que el primero")
else:
    print ("Los vlaores son iguales. No hay ninguno mayor que el otro.")


