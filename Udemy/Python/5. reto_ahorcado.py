import random

### EL AHORCADO
lista_palabras = ["hola", "pez", "lapicero", "calendario"]
letras_correctas = []
letras_incorrectas = []
lista_oculta = []
intentos = 6

def seleccionar_palabra():
    palabra = random.choice(lista_palabras)
    print(f"Inicio del juego, la palabra tiene {len(palabra)} letras")
    lista_oculta.extend("_" * len(palabra))
    print(" ".join(lista_oculta))
    return palabra

def pedir_letra():
    letra = None
    es_valida = False
    while not es_valida:
        letra = input("Por favor ingrese una letra: ").lower()
        if letra.isalpha() and len(letra)==1:
            es_valida = True
        else:
            letra = input("Ingrese una letra correta: ").lower()
    return letra

def tablero(palabra, letra):
    for num, l in enumerate(palabra):
        if l==letra:
            lista_oculta[num] = letra
    print(" ".join(lista_oculta))


def evaluar_letra(palabra, letra_elegida, intentos):
    if letra_elegida in palabra and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
    elif letra_elegida in palabra and letra_elegida in letras_correctas:
        print("Esa letra ya la usaste, prueba con otra")
    else:
        letras_incorrectas.append(letra_elegida)
        intentos -= 1
    return intentos

def evaluar():
    global intentos 
    palabra = seleccionar_palabra()
    lista_palabra = list(palabra)
    while intentos > 0:
        print('\n' + '*' * 20 + '\n')
        print("Letras correctas: ", " ".join(letras_correctas))
        print("Letras incorrectas: ", " ".join(letras_incorrectas))
        print(f"Vidas: {intentos}")
        letra_elegida = pedir_letra()
        tablero(palabra, letra_elegida)
        intentos = evaluar_letra(palabra, letra_elegida, intentos)
        if lista_oculta == lista_palabra:
            return print("Felicitaciones, ganaste")
        
    return print("Perdiste, te quedaste sin vidas")

evaluar()
        
