#Paso1: pedirle al usuario su peso
peso = int(input("Por favor ingrese su peso en kg: "))

#Paso 2: pedirle al usuario su estatura
estatura = float(input("Por favor ingrese su altura en m: "))

#Paso3: Calcular el IMC
imc = peso/(estatura ** 2)

#Paso4: mostrar el dependiendo el caso 

if imc < 18.5 :
    print("Usted tiene una condición de peso inferor al normal")
elif imc >= 18.5 and imc < 24.9 :
    print("Usted tiene una condición de peso normal")
elif imc >= 25 and imc < 29.9 :
    print("Usted tiene un peso superior al normal")
else:
    print("Usted tiene sobrepso")

print(f"Su índice de masa corporal es de {imc} kg/m2")



#if imc >= 25:
 #   print(f"Tiene sobrepso, su IMC es {imc} kg/m2")
#else :
#    print(f"No tiene sobrepso, su IMC es {imc} kg/m2")



