#NO BORRAR LAS IMPORTACIONES QUE ENCUENTRAN A CONTINUACIÓN. LA FUNCIÓN QUE VA A 
#COMPLETAR NO REQUERIRÁ DE PARÁMETROS DE ENTRADA

#LOS MÓDULOS csv Y json ESTÁN ADJUNTOS POR DEFECTO EN LAS VERSIONES MÁS RECIENTES 
#DE PYTHON (3.x). ASEGÚRESE DE QUE LA VERSIÓN DE PYTHON EN LA QUE USTED HA ESTADO 
#EJECUTANDO SU PROPUESTA DE SOLUCIÓN CONTIENE DICHO MÓDULO

import csv
import json
def clima():
    #A PARTIR DE ACÁ PUEDE ADJUNTAR SU PROPUESTA DE SOLUCIÓN.REMÍTASE AL ENUNCIADO 
    #PARA MÁS DETALLES.
    

    localidades =  ["1", "2" , "3" , "4" , "5"]
    templocalidadUno = []
    templocalidadDos = []
    templocalidadTres = []
    templocalidadCuatro = []
    templocalidadCinco = []

    preslocalidadUno = []
    preslocalidadDos = []
    preslocalidadTres = []
    preslocalidadCuatro = []
    preslocalidadCinco = []

    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for linea in reader:
            if linea[1] == "1":
                templocalidadUno.append(int(linea[2]))
                preslocalidadUno.append(int(linea[3]))
            elif linea[1] == "2":
                templocalidadDos.append(int(linea[2]))
                preslocalidadDos.append(int(linea[3]))
            elif linea[1] == "3":
                templocalidadTres.append(int(linea[2]))
                preslocalidadTres.append(int(linea[3]))
            elif linea[1] == "4":
                templocalidadCuatro.append(int(linea[2]))
                preslocalidadCuatro.append(int(linea[3]))
            elif linea[1] == "5":
                templocalidadCinco.append(int(linea[2]))
                preslocalidadCinco.append(int(linea[3]))
        
    promediotemUno = round(sum(templocalidadUno)/len(templocalidadUno), 1)
    promediotemDos = round(sum(templocalidadDos)/len(templocalidadDos), 1)
    promediotemTres = round(sum(templocalidadTres)/len(templocalidadTres), 1)
    promediotemCuatro = round(sum(templocalidadCuatro)/len(templocalidadCuatro), 1)
    promediotemCinco = round(sum(templocalidadCinco)/len(templocalidadCinco), 1)

    promediopresUno = round(sum(preslocalidadUno)/len(preslocalidadUno), 1)
    promediopresDos = round(sum(preslocalidadDos)/len(preslocalidadDos), 1)
    promediopresTres = round(sum(preslocalidadTres)/len(preslocalidadTres), 1)
    promediopresCuatro = round(sum(preslocalidadCuatro)/len(preslocalidadCuatro), 1)
    promediopresCinco = round(sum(preslocalidadCinco)/len(preslocalidadCinco), 1)

    dicc = {}
    for localidad in localidades:
        if localidad == "1":
            dicc[localidad] = [promediotemUno, promediopresUno]
        elif localidad == "2":
            dicc[localidad] = [promediotemDos, promediopresDos]
        elif localidad == "3":
            dicc[localidad] = [promediotemTres, promediopresTres]
        elif localidad == "4":
            dicc[localidad] = [promediotemCuatro, promediopresCuatro]
        elif localidad == "5":
            dicc[localidad] = [promediotemCinco, promediopresCinco]

    datos = json.dumps(dicc)
   

  
    #RECUERDE QUE SU PROPUESTA DEBE ACCEDER A UN ARCHIVO LLAMADO  "data.csv" 
    #(EL ARCHIVO ESTÁ EN ESTA PLATAFORMA), REALIZAR CÁLCULOS EN CADA FILA CON 
    #DOS DATOS ESPECÍFICOS Y LLEVAR LOS RESULTADOS A UN OBJETO JSON QUE CONTENDRÁ 
    #CINCO LISTAS DE DOS PROMEDIOS CADA UNA. ESTE ES EL OBJETO QUE DEBE RETORNAR.
    promedioTem = []
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for fila in reader:
            new_row = fila[:]
            if fila[1] == "1":
                if int(fila[2]) > promediotemUno:
                    new_row.append("SI")
                    promedioTem.append(new_row)
                elif int(fila[2]) < promediotemUno:
                    new_row.append("NO")
                    promedioTem.append(new_row)
                elif int(fila[2]) == promediotemUno:
                    new_row.append("IGUAL")
                    promedioTem.append(new_row)
            elif fila[1] == "2":
                if int(fila[2]) > promediotemDos:
                    new_row.append("SI")
                    promedioTem.append(new_row)
                elif int(fila[2]) < promediotemDos:
                    new_row.append("NO")
                    promedioTem.append(new_row)
                elif int(fila[2]) == promediotemDos:
                    new_row.append("IGUAL")
                    promedioTem.append(new_row)
            elif fila[1] == "3":
                if int(fila[2]) > promediotemTres:
                    new_row.append("SI")
                    promedioTem.append(new_row)
                elif int(fila[2]) < promediotemTres:
                    new_row.append("NO")
                    promedioTem.append(new_row)
                elif int(fila[2]) == promediotemTres:
                    new_row.append("IGUAL")
                    promedioTem.append(new_row)
            elif fila[1] == "4":
                if int(fila[2]) > promediotemCuatro:
                    new_row.append("SI")
                    promedioTem.append(new_row)
                elif int(fila[2]) < promediotemCuatro:
                    new_row.append("NO")
                    promedioTem.append(new_row)
                elif int(fila[2]) == promediotemCuatro:
                    new_row.append("IGUAL")
                    promedioTem.append(new_row)
            elif fila[1] == "5":
                if int(fila[2]) > promediotemCinco:
                    new_row.append("SI")
                    promedioTem.append(new_row)
                elif int(fila[2]) < promediotemCinco:
                    new_row.append("NO")
                    promedioTem.append(new_row)
                elif int(fila[2]) == promediotemCinco:
                    new_row.append("IGUAL")
                    promedioTem.append(new_row)

    promedioPresion = []
    for fila in promedioTem:
            new_row = fila[:]
            if fila[1] == "1":
                if int(fila[3]) > promediopresUno:
                    new_row.append("SI")
                    promedioPresion.append(new_row)
                elif int(fila[3]) < promediopresUno:
                    new_row.append("NO")
                    promedioPresion.append(new_row)
                elif int(fila[3]) == promediopresUno:
                    new_row.append("IGUAL")
                    promedioPresion.append(new_row)
            elif fila[1] == "2":
                if int(fila[3]) > promediopresDos:
                    new_row.append("SI")
                    promedioPresion.append(new_row)
                elif int(fila[3]) < promediopresDos:
                    new_row.append("NO")
                    promedioPresion.append(new_row)
                elif int(fila[3]) == promediopresDos:
                    new_row.append("IGUAL")
                    promedioPresion.append(new_row)
            elif fila[1] == "3":
                if int(fila[3]) > promediopresTres:
                    new_row.append("SI")
                    promedioPresion.append(new_row)
                elif int(fila[3]) < promediopresTres:
                    new_row.append("NO")
                    promedioPresion.append(new_row)
                elif int(fila[3]) == promediopresTres:
                    new_row.append("IGUAL")
                    promedioPresion.append(new_row)
            elif fila[1] == "4":
                if int(fila[3]) > promediopresCuatro:
                    new_row.append("SI")
                    promedioPresion.append(new_row)
                elif int(fila[3]) < promediopresCuatro:
                    new_row.append("NO")
                    promedioPresion.append(new_row)
                elif int(fila[3]) == promediopresCuatro:
                    new_row.append("IGUAL")
                    promedioPresion.append(new_row)
            elif fila[1] == "5":
                if int(fila[3]) > promediopresCinco:
                    new_row.append("SI")
                    promedioPresion.append(new_row)
                elif int(fila[3]) < promediopresCinco:
                    new_row.append("NO")
                    promedioPresion.append(new_row)
                elif int(fila[3]) == promediopresCinco:
                    new_row.append("IGUAL")
                    promedioPresion.append(new_row)


    header.append("above_avg_temp")
    with open('data_nuevo.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(header)
        writer.writerows(promedioTem)

    header.append("above_avg_pres")
    with open('data_nuevo.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(header)
        writer.writerows(promedioPresion)
    
    #SU SOLUCIÓN TAMBIÉN DEBE ESTAR EN CAPACIDAD DE CREAR UN ARCHIVO CSV
    #QUE DEBE LLAMARSE "data_nuevo.csv" A PARTIR DE "data.csv" CON LAS 
    #ESPECIFICACIONES INDICADAS EN EL ENUNCIADO
    
    return datos

localidades =  ["1", "2" , "3" , "4" , "5"]
templocalidadUno = []
templocalidadDos = []
templocalidadTres = []
templocalidadCuatro = []
templocalidadCinco = []

preslocalidadUno = []
preslocalidadDos = []
preslocalidadTres = []
preslocalidadCuatro = []
preslocalidadCinco = []

with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for linea in reader:
        #print(fila)
        if linea[1] == "1":
            templocalidadUno.append(int(linea[2]))
            preslocalidadUno.append(int(linea[3]))
        elif linea[1] == "2":
            templocalidadDos.append(int(linea[2]))
            preslocalidadDos.append(int(linea[3]))
        elif linea[1] == "3":
            templocalidadTres.append(int(linea[2]))
            preslocalidadTres.append(int(linea[3]))
        elif linea[1] == "4":
            templocalidadCuatro.append(int(linea[2]))
            preslocalidadCuatro.append(int(linea[3]))
        elif linea[1] == "5":
            templocalidadCinco.append(int(linea[2]))
            preslocalidadCinco.append(int(linea[3]))


promediotemUno = round(sum(templocalidadUno)/len(templocalidadUno), 1)
promediotemDos = round(sum(templocalidadDos)/len(templocalidadDos), 1)
promediotemTres = round(sum(templocalidadTres)/len(templocalidadTres), 1)
promediotemCuatro = round(sum(templocalidadCuatro)/len(templocalidadCuatro), 1)
promediotemCinco = round(sum(templocalidadCinco)/len(templocalidadCinco), 1)

promediopresUno = round(sum(preslocalidadUno)/len(preslocalidadUno), 1)
promediopresDos = round(sum(preslocalidadDos)/len(preslocalidadDos), 1)
promediopresTres = round(sum(preslocalidadTres)/len(preslocalidadTres), 1)
promediopresCuatro = round(sum(preslocalidadCuatro)/len(preslocalidadCuatro), 1)
promediopresCinco = round(sum(preslocalidadCinco)/len(preslocalidadCinco), 1)

dicc = {}
for localidad in localidades:
    if localidad == "1":
        dicc[localidad] = [promediotemUno, promediopresUno]
    elif localidad == "2":
        dicc[localidad] = [promediotemDos, promediopresDos]
    elif localidad == "3":
        dicc[localidad] = [promediotemTres, promediopresTres]
    elif localidad == "4":
        dicc[localidad] = [promediotemCuatro, promediopresCuatro]
    elif localidad == "5":
        dicc[localidad] = [promediotemCinco, promediopresCinco]

    #print(dicc)
json.dumps(dicc)
print(json.dumps(dicc))


promedioTem = []
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for fila in reader:
        new_row = fila[:]
        if fila[1] == "1":
            if int(fila[2]) > promediotemUno:
                new_row.append("SI")
                promedioTem.append(new_row)
            elif int(fila[2]) < promediotemUno:
                new_row.append("NO")
                promedioTem.append(new_row)
            elif int(fila[2]) == promediotemUno:
                new_row.append("IGUAL")
                promedioTem.append(new_row)

        elif fila[1] == "2":
            if int(fila[2]) > promediotemDos:
                new_row.append("SI")
                promedioTem.append(new_row)
            elif int(fila[2]) < promediotemDos:
                new_row.append("NO")
                promedioTem.append(new_row)
            elif int(fila[2]) == promediotemDos:
                new_row.append("IGUAL")
                promedioTem.append(new_row)
        elif fila[1] == "3":
            if int(fila[2]) > promediotemTres:
                new_row.append("SI")
                promedioTem.append(new_row)
            elif int(fila[2]) < promediotemTres:
                new_row.append("NO")
                promedioTem.append(new_row)
            elif int(fila[2]) == promediotemTres:
                new_row.append("IGUAL")
                promedioTem.append(new_row)
        elif fila[1] == "4":
            if int(fila[2]) > promediotemCuatro:
                new_row.append("SI")
                promedioTem.append(new_row)
            elif int(fila[2]) < promediotemCuatro:
                new_row.append("NO")
                promedioTem.append(new_row)
            elif int(fila[2]) == promediotemCuatro:
                new_row.append("IGUAL")
                promedioTem.append(new_row)
        elif fila[1] == "5":
            if int(fila[2]) > promediotemCinco:
                new_row.append("SI")
                promedioTem.append(new_row)
            elif int(fila[2]) < promediotemCinco:
                new_row.append("NO")
                promedioTem.append(new_row)
            elif int(fila[2]) == promediotemCinco:
                new_row.append("IGUAL")
                promedioTem.append(new_row)

promedioPresion = []
for fila in promedioTem:
        new_row = fila[:]
        if fila[1] == "1":
            if int(fila[3]) > promediopresUno:
                new_row.append("SI")
                promedioPresion.append(new_row)
            elif int(fila[3]) < promediopresUno:
                new_row.append("NO")
                promedioPresion.append(new_row)
            elif int(fila[3]) == promediopresUno:
                new_row.append("IGUAL")
                promedioPresion.append(new_row)
        elif fila[1] == "2":
            if int(fila[3]) > promediopresDos:
                new_row.append("SI")
                promedioPresion.append(new_row)
            elif int(fila[3]) < promediopresDos:
                new_row.append("NO")
                promedioPresion.append(new_row)
            elif int(fila[3]) == promediopresDos:
                new_row.append("IGUAL")
                promedioPresion.append(new_row)
        elif fila[1] == "3":
            if int(fila[3]) > promediopresTres:
                new_row.append("SI")
                promedioPresion.append(new_row)
            elif int(fila[3]) < promediopresTres:
                new_row.append("NO")
                promedioPresion.append(new_row)
            elif int(fila[3]) == promediopresTres:
                new_row.append("IGUAL")
                promedioPresion.append(new_row)
        elif fila[1] == "4":
            if int(fila[3]) > promediopresCuatro:
                new_row.append("SI")
                promedioPresion.append(new_row)
            elif int(fila[3]) < promediopresCuatro:
                new_row.append("NO")
                promedioPresion.append(new_row)
            elif int(fila[3]) == promediopresCuatro:
                new_row.append("IGUAL")
                promedioPresion.append(new_row)
        elif fila[1] == "5":
            if int(fila[3]) > promediopresCinco:
                new_row.append("SI")
                promedioPresion.append(new_row)
            elif int(fila[3]) < promediopresCinco:
                new_row.append("NO")
                promedioPresion.append(new_row)
            elif int(fila[3]) == promediopresCinco:
                new_row.append("IGUAL")
                promedioPresion.append(new_row)


header.append("above_avg_temp")
with open('data_nuevo.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    writer.writerows(promedioTem)

header.append("above_avg_pres")
with open('data_nuevo.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    writer.writerows(promedioPresion)




# print(promedioTem)
# print(promedioPresion)






