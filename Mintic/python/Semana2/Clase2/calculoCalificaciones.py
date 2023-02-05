# ejercicio 4: hacer un sistema de calificaciones
    # pedir la calificación de un examen del usuario (0-5)
    #0-3 imprimir insuficiente (3 no incluido)
    #3-4 imprimir aceptatbal (4 no incluido)
    #4-4.5 imprimir sobresaliente (4.5 no incluido)
    #4.5-5 imprimir excelente
    # en cualquier otro rango imprimir calificación invalida

# ejercicio 4

calificacion = float(input("Por favor ingrese la calificación del exámen: "))
if calificacion >= 0 and calificacion <=5:
    if calificacion >= 0 and calificacion < 3 :
        print ("Su calificación es insuficiente")
    elif calificacion >= 3 and calificacion < 4:
        print ("Su calificación es aceptable")
    elif calificacion >= 4 and calificacion < 4.5:
        print ("Su calificación es sobresaliente")
    else:
        print ("Su calificación es excelente")
else:
    print("Calificación inválida")

  