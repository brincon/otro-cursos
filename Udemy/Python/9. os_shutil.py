import os
import shutil
import send2trash

print(os.getcwd())

# archivo = open("curso.txt", "w")
# archivo.write("archivo de prueba")
# archivo.close()

# print(os.listdir())

# mueve el archivo a la nueva ruta
#shutil.move("curso.txt", "C:\\Users\\brend\\OneDrive\\Documentos")

# # elimina un archivo en una ruta
# os.unlink()
# #elimina una carpeta vacia
# os.rmdir()
# #elimina una carpeta
# os.remove()

# #eliminar todo lo que se encuentre dentro de una ruta
# shutil.rmtree()

# # envia a la papelera de reciclaje
# send2trash.send2trash("curso.txt")

print(os.walk("C:\\Users\\brend\\OneDrive\\Documentos\\GitHub\\pythonbrenda\\Udemy\\Python\\carpeta_superior"))

ruta = "C:\\Users\\brend\\OneDrive\\Documentos\\GitHub\\pythonbrenda\\Udemy\\Python\\carpeta_superior"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son:")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son:")
    for arc in archivo:
        print(f"\t{arc}")
    print("\n")



