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

# sobreescribe
# mi_archivo = open(archivo, w)
# print(mi_archivo.write("Hola"))

# linea al final
# mi_archivo = open(archivo, a)
# print(mi_archivo.write("Hola"))


carpeta = Path('C:/Users/brend/OneDrive/Documentos/GitHub/pythonbrenda/Udemy/Python/text.txt')
# lee el contenido
print(carpeta.read_text())

# nombre del archivo completo
print(carpeta.name)

# nombre del archivo .txt
print(carpeta.suffix)

# nombre del archivo text sin extensión
print(carpeta.stem)

# nombre del archivo text
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Este archivo no existe")

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)

## base 
base = Path.home()
# concatena en ruta y se puede un path dentro de otro
guia = Path("Barcelona", "Europa", Path("libro.txt"))
print(base)
print(guia.parent.parent)

#revisar todas las rutas
guia = Path(Path.home(), "Europa")
### para todos el directorio guia y sus subdirectorios
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

## también rutas relativas
guia = Path("Europa", "españa", "Barcelona", "libro.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa","España"))
print(en_europa)
print(en_espania)