import random
from statistics import median

def lanzar_dados():
    numero1 = random.randint(1,6)
    numero2 = random.randint(1,6)
    
    return numero1, numero2

def evaluar_jugada(numero1, numero2):
    suma_dados = numero1 + numero2
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 or suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif suma_dados >= 10:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
random.choice

num1,num2 = lanzar_dados()
print(num1, num2)
evaluar_jugada(num1, num2)


def devolver_distintos(num1, num2, num3):
    lista = [num1, num2, num3]
    suma = sum(lista)
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return (lista[1])


numero = devolver_distintos(4,8,2)
print(numero)

def palabras_sin_repetir(nombre):
    nombre.split()
    conjunto = set(nombre)
    lista = list(conjunto)
    lista.sort
    return lista

nombre = print(palabras_sin_repetir("brendaa"))

def ceros_seguidos(*args):
    numero = []
    for num in args:
        if len(numero) < 2:
            numero.append(num)
        elif len(numero) == 2:
            if numero[0] == 0 and numero[1] == 0:
                return True
            else:
                numero.pop(0)
                numero.append(num)
    return False

def ceros_vecinos(*args):
    contador = 0
    for i in args:
        if args[contador] == 0 and args[contador+1] == 0:
            return True
        else:
            contador += 1

lista = [1,2,0,0,3,4]
print(ceros_seguidos(6,0,5,1,0,3,0,1))


def contar_primos(numero):
    contador = 0
    for i in range(0, numero+1):
        if i == 0 or i ==1:
            print(i)
            continue
        elif i % 2 != 0:
            print("primo", i)
            contador += 1
    return contador

def contar_primos(numero):
    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0
    
    while iteracion <= numero:

        for i in range(3, numero+1, 2):
            if iteracion % i == 0:
                iteracion +=2
                break
            else:
                primos.append(iteracion)
                iteracion += 2
    print(primos)
        
    return len(primos)


print(contar_primos(6))