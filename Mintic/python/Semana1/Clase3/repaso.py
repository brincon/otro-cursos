edad1 = input("ingrese su edad:" )
edad2 = input("ingrese su edad:" )

diferenciaedad= int(edad1) - int(edad2)

print(f"la diferencia en las edades es de {diferenciaedad} años")

# imrpimir varios textos separados por espacios
print("texto1", "texto2")

# concatenar textos
primerTexto = "hola "
segundoTexto = "mundo"
holamundo = primerTexto + segundoTexto
print (holamundo)

# formatear textos con variables
miedad = 10
print(f"yo tengo {miedad} años")

# nombramiento de variables
# manera 1: PascalCase
VariablePascalCase ="soy un variable con todas las iniciales en mayuscualas"

# manera 2: camelCase
variableCamelCase = "primera palabra todo minuscula y las siguientes palabras con la inicial mayuscula"

# manera 3: snake_case
varible_snake_case = "poner las palabras separadas por un _"

#Operaciones aritméticas
miEdad = 10
edadDeMiMama = 40
#operación de resta
diferenciaDeEdad =edadDeMiMama - miEdad
#operación de suma
diferenciaDeEdad =edadDeMiMama + miEdad

#operación de multiplicación
variable1 = 10
variable2 = 15.5
multiplicacion = variable1 * variable2
division  = variable1 * variable2 # no dividir por cero porque sale error

#jerarquia de las operaciones: potenciación, multiplicación y división, sumas y restas.
variable1 = 10
variable2 = 50
variable3 = 20.7
variable4 = 10.1

#primero sumar v1 y v2, despues restar v2 y v4 y dividir estos dos resultados
resultado1 = (variable1 + variable2) / (variable3 - variable4)

#comando de input general de tipo texto
inputDeUsuario = input("por favor ingrese un valor")

#comando de input general de tipo numerico
inputNumerico = int(input("por favor ingrese un valor numerico"))
print(inputNumerico)
# los input siempre entran de tipo texto o string, por eso se convierte a entero






