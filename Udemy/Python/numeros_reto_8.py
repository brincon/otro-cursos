def turno_farmacia():
    for num in range(1, 10000):
        yield f"F - {num}"
        
    
def turno_medicamentos():
    for num in range(1, 10000):
        yield f"M - {num}"
        

def turno_cosmetica():
    for num in range(1, 10000):
        yield f"C - {num}"

f = turno_farmacia()
m = turno_medicamentos()
c = turno_cosmetica()


def decorar_turno(funcion):
    
    print("\n" + "*" * 23)
    print("Su número es:")
    if funcion == "1":
        print(next(f))
    elif funcion == "2":
        print(next(m))
    elif funcion == "3":
        print(next(c))
    print("Pronto será atendido")
    print("\n" + "*" * 23)


