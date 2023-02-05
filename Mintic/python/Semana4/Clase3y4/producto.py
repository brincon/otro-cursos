import random

# referencia del productocto REF### 
class Producto:
    def __init__(self, nombre, precio): #init es el constructor a la clase 
        self.nombre = nombre
        self.precio = precio
        self.referencia = "REF"+str(random.randint(1000,10000))
        self.inventario = random.randint(0, 1000)


