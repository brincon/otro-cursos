#imprimir la suma, resta y multiplicación de dos números

def addTwoNumbers(n1, n2):
    suma = n1 + n2
    return suma

#definir la funcion de resta
def subtractwoNumbers(n1, n2):
    resta = n1 - n2
    return resta

#definir la funcion de multiplicacion
def multiplyTwoNumbers(n1, n2):
    multipliacion = n1 * n2
    return multipliacion

# number1 = int(input("Por favor ingrese el primer número: "))
# number2 = int(input("Por favor ingrese el segundo número: "))

# suma = addTwoNumbers(number1, number2)
# resta = subtractwoNumbers (number1, number2)
# multipliacion = multiplyTwoNumbers(number1, number2)

# print("La suma es ", suma)
# print("La resta es ", resta)
# print("La multiplicacion es", multipliacion)

#funcion general para el calculo
def calculateResult (n1, n2, operation):
    result = 0 
    if operation == "s":
        result = addTwoNumbers(n1, n2)
    elif operation == "r":
        result = subtractwoNumbers(n1, n2)
    elif operation == "m":
        result = multiplyTwoNumbers(n1, n2)
    else:
        result = "error"
    return result

#funcion con return
def calculateResult (n1, n2, operation):
    if operation == "s":
        return addTwoNumbers(n1, n2)
    elif operation == "r":
        return subtractwoNumbers(n1, n2)
    elif operation == "m":
        return multiplyTwoNumbers(n1, n2)
    else:
        return "error"
    

number1 = int(input("Por favor ingrese el primer número: "))
number2 = int(input("Por favor ingrese el segundo número: "))

suma = calculateResult (number1, number2, "s")
resta = calculateResult (number1, number2, "r")
multiplicacion = calculateResult(number1, number2, "m")

print("La suma es ", suma)
print("La resta es ", resta)
print("La multiplicacion es", multiplicacion)