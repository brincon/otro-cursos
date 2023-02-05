# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

def tiene_cartas_altas(cartas_siguientes):
    # ACÁ INICIA LA FUNCIÓN
    cartasAltas = ("A", "Q", "J", "K")
    set1 = set(cartas_siguientes)
    set2 = set(cartasAltas)
    resultado = set1 & set2
    #print(len(resultado))
    if len(resultado) > 0:
        return True
    else:
        return False
                
        # elif letra == "J":
        #     cartas_siguientes = baraja[(1+contador):(3+contador)]
        #     contador += 1
        #     print (cartas_siguientes)
        #     for carta in cartas_siguientes:
        #         if carta == 'A' or carta == 'J' or carta == 'Q' or carta == 'K':
        #             print("La siguiente carta es alta no tiene puntaje")
        #             return False
        #         else:
        #             puntaje = 2
        #             print("La siguiente carta no es alta, su puntaje es",puntaje)
        #             return True
        # elif letra == "Q":
        #     cartas_siguientes = baraja[(1+contador):(4+contador)]
        #     contador += 1
        #     print (cartas_siguientes)
        #     for carta in cartas_siguientes:
        #         if carta == 'A' or carta == 'J' or carta == 'Q' or carta == 'K':
        #             print("La siguiente carta es alta no tiene puntaje")
        #             return False
        #         else:
        #             puntaje = 3
        #             print("La siguiente carta no es alta, su puntaje es",puntaje)
        #             return True
        # elif letra == "K":
        #     cartas_siguientes = baraja[(1+contador):(5+contador)]
        #     contador += 1
        #     print (cartas_siguientes)
        #     for carta in cartas_siguientes:
        #         if carta == 'A' or carta == 'J' or carta == 'Q' or carta == 'K':
        #             print("La siguiente carta es alta no tiene puntaje")
        #             return False
        #         else:
        #             puntaje = 4
        #             print("La siguiente carta no es alta, su puntaje es", puntaje)
        #             return True
        # else:
        #     contador += 1
        #     return False
                
    # ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS

def juego(baraja):
    # ACÁ INICIA LA FUNCIÓN
   
    contador = 0
    puntajeJugadorUno = 0
    puntajeJugadorDos = 0

    for letra in baraja:
        #print(letra)
        if letra == 'A':
            cartas_siguientes = baraja[(1+contador)]
            contador += 1
            #print ("las cartas siguientes son ",cartas_siguientes)
            # print("el contador es ", contador)
            if tiene_cartas_altas(cartas_siguientes) == False and len(cartas_siguientes) == 1:
                puntaje = 1
                if contador % 2 == 0:
                    puntajeJugadorDos = puntajeJugadorDos + puntaje
                    # print("punto para el jugador dos :", puntajeJugadorDos)
                else:
                    puntajeJugadorUno = puntajeJugadorUno + puntaje
                    # print("punto para el jugador uno:", puntajeJugadorUno)
            else:
                continue
                    
        elif letra == "J":    
            cartas_siguientes = baraja[(1+contador):(3+contador)]
            contador += 1
            # print ("las cartas siguientes son ",cartas_siguientes)
            # print("el contador es ", contador)
            if tiene_cartas_altas(cartas_siguientes) == False and len(cartas_siguientes) == 2:
                puntaje = 2
                if contador % 2 == 0:
                    puntajeJugadorDos = puntajeJugadorDos + puntaje
                    # print("punto para el jugador dos: ", puntajeJugadorDos)
                else:
                    puntajeJugadorUno = puntajeJugadorUno + puntaje
                    # print("punto para el jugador uno:", puntajeJugadorUno)
            else:
                continue

        elif letra == "Q":
            cartas_siguientes = baraja[(1+contador):(4+contador)]
            contador += 1
            # print ("las cartas siguientes son ",cartas_siguientes)
            # print("el contador es ", contador)
            if tiene_cartas_altas(cartas_siguientes) == False and len(cartas_siguientes) == 3:
                puntaje = 3
                if contador % 2 == 0:
                    puntajeJugadorDos = puntajeJugadorDos + puntaje
                    # print("punto para el jugador dos :", puntajeJugadorDos)
                else:
                    puntajeJugadorUno = puntajeJugadorUno + puntaje
                    # print("punto para el jugador uno: ", puntajeJugadorUno)
            else:
                continue

        elif letra == "K":
            cartas_siguientes = baraja[(1+contador):(5+contador)]
            contador += 1
                # print ("las cartas siguientes son ",cartas_siguientes)
                # print("el contador es ", contador)
            if tiene_cartas_altas(cartas_siguientes) == False and len(cartas_siguientes) == 4:
                puntaje = 4
                if contador % 2 == 0:
                    puntajeJugadorDos = puntajeJugadorDos + puntaje
                        # print("punto para el jugador dos :", puntajeJugadorDos)
                else:
                    puntajeJugadorUno = puntajeJugadorUno + puntaje
                        # print("punto para el jugador uno: ", puntajeJugadorUno)
            else:
                continue
        else:
            contador += 1     

    baraja = (puntajeJugadorUno, puntajeJugadorDos)

    return baraja
    
    # ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS

import numpy as np

# baraja = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# matriz = np.array(baraja)
# repetir = np.tile(matriz, 4)
# np.random.shuffle(repetir)
# baraja = tuple(repetir)
# print(baraja)

#baraja = ('9', '6', '5', '7', 'J', '10', '10', 'K', '8', 'K', '9', 'A', '2', 'K', 'K', '4', '10', 'Q', '10', 'Q', '4', '3', '4', '2', 'A', '7', '2', 'J', '3', '6', '5', '5', 'A', '8', '2', 'A', 'J', '8', '8', '6', '3', '3', '9', '5', '6', '7', 'Q', '9', 'Q', '4', 'J', '7')
baraja = ('Q', '6', '7', '4', 'K', '4', '4', '2', '3', '6', '10', 'Q', '6', '3', '10', 'K', '8', '9', 'J', 'J', '9', '9', '2', 'A', 'K', '5', 'J', '2', 'K', '8', 'A', '5', 'Q', '5', '5', '4', '3', '3', '8', '9', '8', '6', '7', 'Q', 'A', '7', '2', '10', '7', 'A', 'J', '10')

contador = 0
puntajeJugadorUno = 0
puntajeJugadorDos = 0

for letra in baraja:
    print(letra)
    if letra == 'A':
        cartas_siguientes = baraja[(1+contador)]
        contador += 1
        print ("las cartas siguientes son ",cartas_siguientes)
        print("el contador es ", contador)
        if tiene_cartas_altas(cartas_siguientes) == False and len(cartas_siguientes) == 1:
            puntaje = 1
            if contador % 2 == 0:
                puntajeJugadorDos = puntajeJugadorDos + puntaje
                print("punto para el jugador dos :", puntajeJugadorDos)
            else:
                puntajeJugadorUno = puntajeJugadorUno + puntaje
                print("punto para el jugador uno:", puntajeJugadorUno)
        else:
            continue
                
    elif letra == "J":    
        cartas_siguientes = baraja[(1+contador):(3+contador)]
        contador += 1
        print ("las cartas siguientes son ",cartas_siguientes)
        print("el contador es ", contador)
        if tiene_cartas_altas(cartas_siguientes) == False and len(cartas_siguientes) == 2:
            puntaje = 2
            if contador % 2 == 0:
                puntajeJugadorDos = puntajeJugadorDos + puntaje
                print("punto para el jugador dos: ", puntajeJugadorDos)
            else:
                puntajeJugadorUno = puntajeJugadorUno + puntaje
                print("punto para el jugador uno:", puntajeJugadorUno)
        else:
            continue

    elif letra == "Q":
        cartas_siguientes = baraja[(1+contador):(4+contador)]
        contador += 1
        print ("las cartas siguientes son ",cartas_siguientes)
        print("el contador es ", contador)
        if tiene_cartas_altas(cartas_siguientes) == False and len(cartas_siguientes) == 3:
            puntaje = 3
            if contador % 2 == 0:
                puntajeJugadorDos = puntajeJugadorDos + puntaje
                print("punto para el jugador dos :", puntajeJugadorDos)
            else:
                puntajeJugadorUno = puntajeJugadorUno + puntaje
                print("punto para el jugador uno: ", puntajeJugadorUno)
        else:
            continue

    elif letra == "K":
        cartas_siguientes = baraja[(1+contador):(5+contador)]
        contador += 1
        print ("las cartas siguientes son ",cartas_siguientes)
        print("el contador es ", contador)
        if tiene_cartas_altas(cartas_siguientes) == False and len(cartas_siguientes) == 4:
            puntaje = 4
            if contador % 2 == 0:
                puntajeJugadorDos = puntajeJugadorDos + puntaje
                print("punto para el jugador dos :", puntajeJugadorDos)
            else:
                puntajeJugadorUno = puntajeJugadorUno + puntaje
                print("punto para el jugador uno: ", puntajeJugadorUno)
        else:
            continue
    else:
        contador += 1
    

puntaje = (puntajeJugadorUno, puntajeJugadorDos)

print(puntaje)

print(juego(baraja))





    



          
    