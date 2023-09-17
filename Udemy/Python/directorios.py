import os

## Cambiar de directorio os.chdir(ruta//carpeta//)
## Crear archivos os.makedirs(ruta//carpeta//carpetacreada)

ruta = "C:\\Users\\brend\\OneDrive\\Documentos\\GitHub\\pythonbrenda\\Udemy\\Python\\prueba.txt"
## trae el nombre del archivo
elemento = os.path.basename(ruta)

## trae la ruta donde se encuentra el archivo
elemento = os.path.dirname(ruta)

## trae una tupla, con la ruta donde se encuentra el archivo y su nombre
elemento = os.path.split(ruta)

from pathlib import Path, PureWindowsPath
carpeta = Path('C:/Users/brend/OneDrive/Documentos/GitHub/pythonbrenda/Udemy/Python')
archivo = carpeta / 'prueba.txt'

# mi_archivo = open(archivo)
# print(mi_archivo.read())

carpeta = Path('C:/Users/brend/OneDrive/Documentos/GitHub/pythonbrenda/Udemy/Python/text.txt')
# lee el contenido
print(carpeta.read_text())

# nombre del archivo
print(carpeta.name)

# nombre del archivo .txt
print(carpeta.suffix)

# nombre del archivo text
print(carpeta.stem)

# nombre del archivo text
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Este archivo no existe")

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)