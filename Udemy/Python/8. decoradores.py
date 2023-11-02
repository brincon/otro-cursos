#Los decoradores son funciones que modifican el comportamiento de otras
#funciones. las funciones son objetos

# def mayuscula(texto):
#     print(texto.upper())

# def mayuscula(texto):
#     print(texto.lower())


# mi_funcion = mayuscula

# mi_funcion('python')

# def una_funcion(funcion):
#     return funcion

# una_funcion(mayuscula("probando"))

# def cambiar_letras(tipo):
#     def mayuscula(texto):
#         print(texto.upper())

#     def miniscula(texto):
#         print(texto.lower())

#     if tipo == "may":
#         return mayuscula
    
#     elif tipo == "min":
#         return miniscula

# operacion = cambiar_letras("may")
# operacion("palabra")


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra_funcion

# @decorar_saludo
def mayuscula(texto):
    print(texto.upper())

# @decorar_saludo 
def miniscula(texto):
    print(texto.lower())

# mayuscula("Python")

mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula("python")
mayuscula_decorada("python")

