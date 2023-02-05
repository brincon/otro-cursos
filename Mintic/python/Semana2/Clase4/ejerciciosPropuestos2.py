#punto11
#punto16

# numero1 = int(input("Por favor ingrese un número: "))
# numero2 = int(input("Por favor ingrese un número: "))
# print ("La suma de los números es: ", numero1 + numero2)
# pregunta = input("Desea realizar la operación de nuevo: ").lower()

# while pregunta != "no":
#     numero1 = int(input("Por favor ingrese un número: "))
#     numero2 = int(input("Por favor ingrese un número: "))
#     print ("La suma de los números es: ", numero1 + numero2)
#     pregunta = input("Desea realizar la operación de nuevo: ").lower()

#punto17
# salario = float(input("Por favor ingrese su salario anual actual: "))
# desempeño = float(input("Por favor ingrese su calificación de desempeño: "))
# if desempeño ==1:
#     aumento = salario * 6/100 
# elif desempeño == 2:
#     aumento = salario * 4/100
# elif desempeño == 3:
#     aumento = salario * 1.5/100

# print("El aumento de su salario es:", aumento)

#punto18

# tem = float(input("Por favor ingrese la temperatura: "))

# if tem > 95:
#     print("¡Visite nuestras tiendas!")
# elif tem >= 80 and tem <= 95:
#     print("La actividad apropiada es natación")
# elif 60 <= tem <80:
#     print("La actividad apropiada es tenis")
# elif 40 <= tem <60:
#     print("La actividad apropiada es golf")
# elif 20 <= tem <40:
#     print("La actividad apropiada es esquí")
# elif tem < 20:
#     print("¡Visite nuestras tiendas!")

#punto19
# adivina = input ("Ingrese piedra(R), papel(P) o tijera (S): ")
# adivina1 = input("Ingrese piedra(R), papel(P) o tijera (S): ")
# if adivina == "R" and adivina1 ==  "P":
#     print("Ganó el jugador 2")
# elif adivina == "R" and adivina1 == "S":
#     print("Ganó el jugador 1")
# elif adivina == "P" and adivina1 == "R":
#     print("Ganó el jugador 1")
# elif adivina == "P" and adivina1 == "S":
#     print("Ganó el jugador 2")
# elif adivina == "S" and adivina1 == "R":
#     print("Ganó el jugador 2")
# elif adivina == "S" and adivina1 == "P":
#     print("Ganó el jugador 1")
# else:
#     print("Empate")

#punto20
#alguien gane dos o tres juegos
# cont = 0
# cont1  = 0
# juegos = 0
# while (cont != 2 or cont1 != 2) and juegos != 3:
#     adivina = input ("Ingrese piedra(R), papel(P) o tijera (S): ")
#     adivina1 = input("Ingrese piedra(R), papel(P) o tijera (S): ")
#     print ("Juegos", juegos)
#     if adivina == "R" and adivina1 ==  "P":
#         cont1 = cont1 + 1
#         print("Ganó el jugador 2")
#         print (cont1)
#         print (cont)
#     elif adivina == "R" and adivina1 == "S":
#         cont = cont + 1
#         print("Ganó el jugador 1")
#         print (cont1)
#         print (cont)
#     elif adivina == "P" and adivina1 == "R":
#         cont = cont + 1
#         print("Ganó el jugador 1")
#         print (cont1)
#         print (cont)
#     elif adivina == "P" and adivina1 == "S":
#         cont1 = cont1 + 1
#         print("Ganó el jugador 2")
#         print (cont1)
#         print (cont)
#     elif adivina == "S" and adivina1 == "R":
#         cont1 = cont1 + 1
#         print("Ganó el jugador 2")
#         print (cont1)
#         print (cont)
#     elif adivina == "S" and adivina1 == "P":
#         cont = cont + 1
#         print("Ganó el jugador 1")
#         print (cont1)
#         print (cont)
#     else:
#         print("Empate")
#         print (cont1)
#         print (cont)

# if cont > cont1:
#     print("Fin, ganó el jugador 1")
# elif cont1 > cont:
#     print("Fin, ganó el jugador 2")

#punto 20 forma del profe
# cont1 = 0
# cont2 = 0
# while cont1 <2 and cont2<2: #cuando alguno sea 2 nos salimos
    #mismas condiciones que yo
    #los contadores al nivel del if

#punto21
# numer = 0
# while numer != 100:
#     numer = numer + 1
#     print ("I love computer science")
#     print (numer)

#punto22
# candidate = int(input("Por favor ingrese el número de votos: "))
# candidate2 = int(input("Por favor ingrese el número de votos: "))

# if candidate2 > candidate:
#     print("Ganó el candidatos 2")
# elif candidate > candidate2:
#     print("Ganó el candidatos 1")

#punto23
# numperson = int(input("Por favor ingrese el número de personas: "))
# edadperson = []
# while len(edadperson)!= numperson:
#     edadperson.append(int(input("Por favor ingrese la edad de las personas: ")))

# print("El promedio de las edades es:", sum(edadperson)/len(edadperson))

#punto24



