import numeros_reto_8

def preguntar():

    print("Bienvenido")

    while True:
        opciones = input("""
                Por favor seleccione a donde se dirige:
                1. Farmacia
                2. Medicamentos
                3. Cosmetica
            """)
        print(opciones)
        
        try: 
            ["1", "2", "3"].index(opciones)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break
        
    numeros_reto_8.decorar_turno(opciones)


def inicio():

    preguntar()

    while True:
        try:
            otro_turno = input("""
                Quiere sacar otro turno
                [S] SI
                [N] No
            """).upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()






