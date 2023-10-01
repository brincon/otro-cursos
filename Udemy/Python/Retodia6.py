from pathlib import Path
import os

guia = Path('C:/Users/brend/OneDrive/Documentos/GitHub/pythonbrenda/Udemy/Python/Recetas')

def imprime_rutas(ruta):
    ### para todos el directorio guia y sus subdirectorios
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        #print(txt)
        contador += 1
    return contador

def imprime_recetas(ruta):
    for txt in Path(ruta).glob("**/*.txt"):
        print(txt.name)

def lee_recetas(ruta, receta):
    for txt in Path(ruta).glob("**/*.txt"):
        if txt.stem == receta:
            print(txt.read_text())

def elimina_recetas(ruta, receta):
    for txt in Path(ruta).glob("**/*.txt"):
        if txt.stem == receta:
            Path(txt).unlink()

def escribe_receta(ruta, nombre, contenido):
    ruta_receta = Path(ruta, f"{nombre}.txt")
    mi_archivo = open(ruta_receta, 'w')
    mi_archivo.write(contenido)


opcion = True
while not opciones.isnumeric() or int(opciones) not in range(1,7):
    os.system('cls')
    print("--"*40)
    print(" Bienvenido al administrador de recetas ")
    print("--"*40)
    print("\n")
    print(f"Las recetas se encuentran en {guia}")
    print(f"\nEn total tienes: {imprime_rutas(guia)} Recetas ")
    opciones = input("""                     
        Por favor elija alguna opción:
        1. Leer receta
        2. Crear receta
        3. Crear categoría
        4. Eliminar receta
        5. Eliminar categoría
        6. Finaliza programa
    """)

    if opciones == "1":
        categoria = input("\nPor favor elija una categoria: ")

        print(f"\nPara la categoria {categoria} tiene las recetas: ")
        categorias = Path(guia, categoria)
        imprime_recetas(categorias)
        
        receta = input("\nPor favor elige la receta que desea leer: ")
        lee_recetas(categorias, receta)
        
 
    elif opciones == "2":
        categoria = input("Por favor elija una categoria: ")
        categorias = Path(guia, categoria)
        
        nombre_receta = input("Por favor elige el nombre de la nueva receta: ")
        contenido = input("Por favor escribe el contenido de la nueva receta: ")
        escribe_receta(categorias, nombre_receta, contenido)


    elif opciones == "3":
        nueva_categoria = input("Por favor ingrese el nombre de la nueva categoría: ")
        ruta = Path(guia, nueva_categoria)
        Path.mkdir(ruta)


    elif opciones == "4":
        categoria = input("\nPor favor elija una categoria: ")

        print(f"\nPara la categoria {categoria} tiene las recetas: ")
        categorias = Path(guia, categoria)
        imprime_recetas(categorias)
        
        receta = input("\nPor favor elige la receta que desea eliminar: ")
        elimina_recetas(categorias, receta)


    elif opciones == "5":
        categoria = input("\nPor favor elija una categoria: ")
        categorias = Path(guia, categoria)
        Path.rmdir(categorias)

   
    elif opciones == "6":
        opcion = False
    
    input("Por favor seleccione enter para volver al menu inicial")


