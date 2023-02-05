#Paso1: pedirle al usuario su peso
peso = int(input("Por favor ingrese su peso en kg: "))

#Paso 2: pedirle al usuario su estatura
estatura = float(input("Por favor ingrese su altura en m: "))

#Paso3: Calcular el IMC
imc = peso/(estatura ** 2)

#Paso4: mostrar el dependiendo el caso 
if imc >= 25:
    print(f"Tiene sobrepso, su IMC es {imc} kg/m2")
else :
    print(f"No tiene sobrepso, su IMC es {imc} kg/m2")



