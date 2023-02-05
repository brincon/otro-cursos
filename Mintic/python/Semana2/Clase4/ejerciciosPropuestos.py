#ejercicio1
#convertir de grados celsius a farenheit
gradosCelsius = float(input("Por favor ingrese la temperatura en ºC: "))
gradosFarenheit = (gradosCelsius * 9/5) + 32
print(f"La temperatura en ºF es {gradosFarenheit}")

#punto2
#adivinar un número entre 1 y 9
adivinacion = 3
usuario = int(input("Por favor intente adivinar un número: "))
while adivinacion != usuario:
    if 1 <= usuario <= 9:
        usuario = int(input("Por favor intente adivinar nuevamente el número: "))
    elif 1 < usuario > 9:
        print("Numero fuera del rango, debe ser entre 1 y 9")
        usuario = int(input("Por favor intente adivinar nuevamente el número: "))

print ("Adivinaste")

#punto3
#Contar los numeros de una serie si son par o impar
numeroUsiario = int(input("Por favor ingrese un número: "))
numero = numeroUsiario % 2
if numero == 0:
    print ("El número es par")
else:
    print("El número es impar")

#punto4
#imprimir los numeros del 0 al 6 excepto 3 y 6
listaOfNumerbs = [0, 1, 2, 3, 4, 5, 6]
for i in listaOfNumerbs:
    if i != 3 and i !=6:
        print(i)

#punto5
#secuencia 0 y 50, el siguiente numero se encuentra sumando los dos anteriores

secuencia = [0, 1]
for i in secuencia:
    if len(secuencia) <= 2:
        secuencia.append(sum(secuencia))    
    elif len(secuencia) > 2 and len(secuencia) <= 50:
        ultimonumero = len(secuencia) - 1
        penultimonumero = len(secuencia) - 2
        valor = secuencia[(ultimonumero)]
        #print (valor)
        valor2 = secuencia[(penultimonumero)]
        #print(valor2)
        agregar = valor + valor2
        #print(agregar)
        secuencia.append(agregar)
print(secuencia)

#punto 5 profesor
listFibonacci = [0, 1]
cont = 1
while len(listFibonacci)< 50:
    listFibonacci.append(listFibonacci[cont]+ listFibonacci[cont-1])
    cont += 1

print (listFibonacci)

#punto6
#edad de un perro

ageDog = float(input("Por favor ingrese la edad del perro en años: "))
menorDosAge = ageDog * 10.5
if ageDog <= 2:
    conversionAge = ageDog * 10.5
    print ("La edad del perro en años perros es :", conversionAge)
elif ageDog > 2:
    conversionAge1 = (2 * 10.5) + (ageDog - 2) * 4
    print ("La edad del perro en años perros es :", conversionAge1)

#punto7
#verificar si es vocal o consonante
letra = input("Por favor ingrese una letra: ")
if letra == "a" or letra== "e" or letra == "i" or letra == "o" or letra == "u":
    print ("La letra que ingresó es una vocal")
else:
    print ("La letra que ingresó es una consonante")

#punto8
# imprimir el orden de las variables
variable1 = int(input("Por favor ingrese una variable entera: "))
variable2 = int(input("Por favor ingrese una variable entera: "))
variable3 = int(input("Por favor ingrese una variable entera: "))
variable4 = int(input("Por favor ingrese una variable entera: "))

lis = [variable1, variable2, variable3, variable4]
ordenados = sorted(lis)
reverso = sorted(lis, reverse=True)
if lis == ordenados:
    print("Los número ingresados estan ordenados de manera ascendente")
elif lis == reverso:
    print("Los número ingresados estan ordenados de manera descendente")
else:
    print("Los número ingresados estan desordenados")

#punto9

ventas = float(input("Por favor ingrese sus ventas: "))

if ventas < 5000000:
    comision = ventas * 2.5/100
elif 5000000 <= ventas < 15000000:
    comision = ventas * 7.5/100
elif 15000000 <= ventas < 30000000:
    comision = ventas * 11.5/100
elif 30000000 <= ventas < 55000000:
    comision = ventas * 15/100
else:
    comision = 3050000 + (7.5/100) * (ventas - 55000000)

print("Su comisión es:", comision)

#punto10
#tabla de multiplicar
numero = int(input("Por favor ingrese un número: "))
count = 1

while numero != (count -1):
    multiplicacion = count * numero
    print (numero, "*", count, "=", multiplicacion, )
    count = count + 1
print ("Esta fue la tabla de multiplicar")

#punto12
calificaciones = [1, 2, 3, 4, 5, 5, 3, 4]
mayores = []
menores = []
for i in calificaciones:
    if i >= 3:
        mayores.append(i)
    elif i < 3:
        menores.append(i)

print ("El promedio de los que obtuvieron calificaciones mayores a 3 es:", sum(mayores)/len(mayores))
print ("El promedio de los que obtuvieron calificaciones menor a 3 es:", sum(menores)/len(menores))

#punto13
negativo = int(input("Por favor ingrese un número: "))
x = []
while negativo >= 0:
    x.append(negativo)
    negativo = int(input("Por favor ingrese un número: "))

print ("La suma de los números ingresados es:", sum(x))

#punto14
usua = None
while usua != "END":
    usua = input("Por favor ingrese una palabra: ")
print ("I am done")

#punto15
enteros = [3, 4 ,5 ,6 ,7 ,8, 1, 2, 3]
pares = []
impares = []
for i in enteros:
    if i%2:
        pares.append(i)
    else:
        impares.append(i)
print ("La suma de los enteros pares es:", sum(pares))
print ("La suma de los enteros impares es:", sum(impares))





