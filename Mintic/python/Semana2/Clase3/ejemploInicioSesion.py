# pedirle al usuario que ingrese su contraseña
# si la contraseña conincide con storedPassword,
# mostrarle un mensaje de inicio de sesión correcto

# si la contraseña no coincie, mostrarle un mensaje de error
# y pedirle la contraseña nuevamente

#passwordUsuario = None
#storedPassword = "123abc"

#while passwordUsuario != storedPassword:
#   passwordUsuario = input("Por favor ingrese su contraseña: ")
#    if passwordUsuario == storedPassword:
#        print("Inicio de sesion correcto")
#    else:
#        print("la contraseña no coincide, ingresela nuevamente")

#opcion 2 profe y agregar que solo tiene 3 intentos
maxRetries = 3
storedPassword = "123abc"
userPassword = input("Por favor ingrese su contraseña: ")
cont = 1
#cuando las contraseñas diferentes y se haya equivocado menos de 3 veces,
#son las dos condiones, el while se ejecuta tantas veces como la condicion
#sea falsa
while storedPassword != userPassword and cont < maxRetries:
    print("la contraseña no coincide")
    cont = cont + 1
#   cont +=1
    print ("valor del contador", cont)
    userPassword = input("Por favor ingrese nuevamente su contraseña: ")

if cont >= maxRetries:
    print("Te equivocaste más de 3 veces, estas bloqueado")
else:
    print("Inicio de sesión correcto")

