#paso1: pedirle al usuario los ingresos
ingresos = float(input("Por favor digite los ingresos de la empresa: "))
#paso2: pedirle al usuario los costos
costos = float(input("Por favor digite los costos de la empresa: "))
#paso#: calcular la utilidad bruta ingresos-costos
utilidadBruta= ingresos - costos
print (f"La utilidad bruta de la empresa es: {utilidadBruta} pesos")
#pedirle al usuario los gastos
gastos = float(input("Por favor digite los gastos de la empresa: "))
#calcular la utilidad operativa, utilidad bruta -gastos
utilidadOperativa = utilidadBruta - gastos
print (f"La utilidad operativa de la empresa es: {utilidadOperativa} pesos")
#calcular el impuesto a la renta 30%, utilidad operativa* 30%
impuesto = utilidadOperativa * 30/100
print (f"El impuesto de renta que debe pagar la empresa es: {impuesto} pesos")

#calcular utilidad neta, utilidad bruta - impuesto a la renta
utilidadNeta = utilidadOperativa  - impuesto

print (f"La utilidad neta de la empresa es: {utilidadNeta} pesos")

#https://github.com/danyel117/MisionTIC

