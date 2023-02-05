import random

# hacer un juego de piedra, papel o tijera contra el computador.
# el computador escoge aleatoriamente, piedra, papel o tijera
# y debe pedir al usuario su input
# el juego debe terminar cuando alguno de los dos gane 2 de 3 partidas

def adivineRPS():
    opciones = ["R", "P", "S"]
    contador = 1
    juegosGanadospc = 0
    juegosGanadosUsuario = 0
    
    while contador <= 3 and (juegosGanadospc < 3 or juegosGanadosUsuario < 3):
        opcionPc = random.choice(opciones)
        opcionUsuario = str(input("Ingrese piedra(R), papel(P) o tijera (S): "))       
        if opcionPc == "R" and opcionUsuario == "R":
            print ("Empate")
        elif opcionPc == "P" and opcionUsuario == "P":
            print ("Empate")
        elif opcionPc == "S" and opcionUsuario == "S":
            print ("Empate")

        elif opcionPc == "R" and opcionUsuario == "P":
            juegosGanadosUsuario = juegosGanadosUsuario + 1
            print("Ganaste la partida")
        elif opcionPc == "R" and opcionUsuario == "S":
            juegosGanadospc = juegosGanadospc + 1
            print("Perdiste la partida")

        elif opcionPc == "P" and opcionUsuario == "R":
            juegosGanadosUsuario = juegosGanadosUsuario + 1
            print("Ganaste la partida")
        elif opcionPc == "P" and opcionUsuario == "S":
            juegosGanadospc = juegosGanadospc + 1
            print("Perdiste la partida")
        
        elif opcionPc == "S" and opcionUsuario == "R":
            juegosGanadosUsuario = juegosGanadosUsuario + 1
            print("Ganaste la partida")
        elif opcionPc == "S" and opcionUsuario == "P":
            juegosGanadospc = juegosGanadospc + 1
            print("Perdiste la partida")

        contador = contador + 1 
    
    if juegosGanadosUsuario == 2:
        return "Ganaste 2 de 3 juegos"
    elif juegosGanadospc == 2:
        return "Perdiste 2 de 3 juegos"
    else:
        return "Empate"

#funcion para que el computado escoja piedra, papel o tijera
def machineSelection():
    randomNumber = random.randint(1, 3)
    if randomNumber == 1: #1 = rock
        return "R"
    elif randomNumber == 2: #2 = paper
        return "P"
    elif randomNumber == 3: #3 = scissors
        return "S"

def evaluateRockPaperScissorsConditions(machine, user):
    if machine == user:
        return "empate"

    if machine == "R" and user == "S":
        return "machine"
    elif user == "R" and machine == "S":
        return "user"

    if machine == "P" and user == "R":
        return "machine"
    elif user == "P" and machine == "R":
        return "user"

    if machine == "S" and user == "P":
        return "machine"
    elif user == "S" and machine == "P":
        return "user"

def playRockPaperScissors():
    contMachine = 0
    contUser = 0
    while contMachine<2 and contUser<2:
        machine = machineSelection()
        user = input("Por favor ingrese su selección (R,P,S): ")
        print("la máquina seleccionó ", machine)
        result = evaluateRockPaperScissorsConditions(machine,user)
        if result == "machine":
            contMachine = contMachine + 1
            print("La máquina gana")
        elif result == "user":
            contUser = contUser + 1 
            print("el usuario gana")
        else:
            print("empate")
        
        print("usr",contUser)
        print("mchn",contMachine)

    if contMachine==2:
        return "machine"
    elif contUser==2:
        return "user"

winner = playRockPaperScissors()
print("El ganador definitivo es: ", winner)

