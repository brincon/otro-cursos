#paso1: pedirle al usuario la cantidad de personas a ingresar
#paso2: en un for de = a N pedir las edades de esas N personas
#paso3: guardar las edades de esa persona enn una lista
#paso4: calcular el promedio de esas edades

numerOfPersons = int(input("Por favor ingrese la cantidad de personas: "))

listOfAges = []
for i in range (0, numerOfPersons):
    #print(i)
    listOfAges.append(int(input("Por favor ingrese la edad de la persona: ")))

average = sum(listOfAges)/len(listOfAges)
print(f"El promedio de las edades es {average} años")



