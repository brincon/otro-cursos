numeroAEncontrar = 7

numeroIngresadoPorElUsuario = int(input("Adivina cuál número está registrado como variable: "))

if numeroIngresadoPorElUsuario > numeroAEncontrar:
    print("El número que estas buscando es mejor al que ingresaste")
elif numeroIngresadoPorElUsuario < numeroAEncontrar:
    print("El número que estás buscando es mayor al que ingresaste")
#elif numeroAEncontrar == numeroIngresadoPorElUsuario:
else:
    print("¡Correcto! El número que ingresaste es el correcto.")

