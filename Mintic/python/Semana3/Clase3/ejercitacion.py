#hacer un juego de adivinanzas
# el número a adivinar es un aleatorio entre 0 y 20
# el código debe generar automaticamente el aleatorio
# y preguntarle al usuario con un input el numero que quiere adivinar
# el juego debe tener un máximo número de intentos
# si me paso del máximo sin adivinar, pierdo
# si adivino, gano

import random

def advinaElNumero():
    numeroAdivinar = random.randint(0, 20)
    numeroUsuario = int(input("Adivine el número entre 0 y 20: "))
    contador = 2
    while numeroAdivinar != numeroUsuario and contador <= 3:
        numeroUsuario = int(input("Por favor intente adivinar nuevamente el número entre 0 y 20: "))
        contador = 1 + contador
    
    if contador >= 4:
        return "Perdiste, te equivocaste 3 veces"
    else:
        return "Adivinaste"

#print(advinaElNumero())
# opcion profesor

def GuessTheNumber(maxRetries):

    numberToGuess = random.randint(0, 20)
    maxGuess = maxRetries
    contUserGuess = 0
    won = False

    while contUserGuess < maxGuess and not won:
        userInput = int(input("Adivina el número entre 0 y 20: "))
        if userInput == numberToGuess:
            print("Has ganado")
            won = True
            return won
        else: 
            print("Respuesta incorrecta")
            contUserGuess = contUserGuess + 1
            print(f"Te quedan {maxGuess - contUserGuess} intentos")

    if contUserGuess == maxGuess:
        print(f"Has perdido, el número a encontrar era {numberToGuess}")
    return won

print(GuessTheNumber(5))




#print(adivineRPS())

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
