#pedirle al usuario dos contraseñas

contraseñasIguales = False

while contraseñasIguales == False:
    contraseña1= input("Ingrese la contraseña1: ")
    contraseña2= input("Ingrese la contraseña2: ")
    if contraseña1 == contraseña2:
        contraseñasIguales = True
    else:
        print("Las contraseñas son diferentes. Por favor ingreselas nuevamente.")
    
print("Las contraseñas coinciden. El registro se ha efectuado de manera correcta.")


