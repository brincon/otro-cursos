#ejercicio 5
# mostrar si un estudiante esta habilitado para presentar el examen
# si el estudiante fue a mas del 75% de las clases puede hacer examen
# si el estudiante fue a menos del 75% de las clases, solo puede hacer el examen si tiene excusa médica

numeroClases = int(input("Por favor ingrese el número de clases: "))
asistencia = int(input("Por favor ingrese la asistencia: "))

porcentajeAsistencia = asistencia / numeroClases

if porcentajeAsistencia >= 0.75:
    print ("Usted esta habilitado para presentar el examen")
elif porcentajeAsistencia < 0.75:
    excusaMedica = input("¿Tiene excusa medica?: ").lower()
    if excusaMedica == "si":
        print ("Usted esta habilitado para presentar el examen")
    else:
        print ("Usted no esta habilitado para presentar el examen")
else:
    print ("Usted no esta habilitado para presentar el examen")

# como lo hizo el profe
if porcentajeAsistencia >= 0.75:
    print ("Usted esta habilitado para presentar el examen")
else:
    excusaMedica = input("¿Tiene excusa medica?: ").lower()
    if excusaMedica == "si" or excusaMedica =="sí":
        print ("Usted esta habilitado para presentar el examen")
    else:
        print ("Usted no esta habilitado para presentar el examen porque el porcentaje de asistencia es muy bajo")
        print("El estudiante solo asistió al {:.2f}% de las clases".format(porcentajeAsistencia*100))







