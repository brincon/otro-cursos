def isPrimeNumber (number):
    #retornar True si el número es primo. False si no es primo
    if number ==1 or number == 0:
        return False
    isPrime = True
    for divisor in range(2, number):
        # print(f"numero: {number}")
        # print(f"divisor: {divisor}")
        # print(f"residuo: {number % divisor}")
        if number % divisor == 0:
            isPrime = False
            return isPrime #se ejecuta hasta que encuentre un primer resultado en cero, no se pone este se ejecuta bien el codigo pero va a evaluar más veces de lo necesario el codigo. 
    return isPrime

#print(isPrimeNumber(3))

# contPrimeNumbers = 0
# numberToEvalute = 1
# sumPrime = []

# while contPrimeNumbers < 4:
#     if isPrimeNumber (numberToEvalute):
#         contPrimeNumbers = contPrimeNumbers + 1
#         print(numberToEvalute)
#         sumPrime.append(numberToEvalute)        
#     numberToEvalute = numberToEvalute + 1
    
# print (sumPrime)

# if isPrimeNumber (sum(sumPrime)):
#     print("La suma tammbien es prima")

# identificar la primera secuencia de números
# primos cuya suma también es prima
# forma profesor 
# contPrimeNumbers = 0
# numberToEvalute = 1
# sumPrime = 0

# while contPrimeNumbers < 20:
#     if isPrimeNumber (numberToEvalute):
#         contPrimeNumbers = contPrimeNumbers + 1
#         sumPrime = sumPrime + numberToEvalute
#         print(numberToEvalute, sumPrime, isPrimeNumber(sumPrime))


#     numberToEvalute = numberToEvalute + 1

#controla el número de True que salgan abajo con el segundo if    
contPrimeNumbers = 0
numberToEvalute = 1
sumPrime = 0
sumPrimeFound = False

while not sumPrimeFound:
    if isPrimeNumber (numberToEvalute):
        contPrimeNumbers = contPrimeNumbers + 1
        sumPrime = sumPrime + numberToEvalute
        print(numberToEvalute, sumPrime, isPrimeNumber(sumPrime))
        if isPrimeNumber (sumPrime) and contPrimeNumbers >=2:
            sumPrimeFound = True

    numberToEvalute = numberToEvalute + 1









