# class Animal:

#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color
        
        

#     def nacer(self):
#         print("Este animal ha nacido")

# class Pajaro(Animal):
#     pass

# # muestra de quien hereda
# print(Pajaro.__bases__)

# # muestra a quien transmite su herencia
# print(Animal.__subclasses__())

# piolin = Pajaro(2, "Amarillo")
# piolin.nacer()
# print(piolin.color)


# class Animal:

#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color
        
#     def nacer(self):
#         print("Este animal ha nacido")

#     def hablar(self):
#         print("Este animal emite un sonido")

# class Pajaro(Animal):
#     #con super se hacen todas las asignaciones heredadas y solo se 
#     # crean las nuevas
#     def __init__(self, edad, color, altura_vuelo):
#         super().__init__(edad, color)
#         self.altura_vuelo = altura_vuelo

#     def hablar(self):
#         print("pio")

#     def volar(self, metros):
#         print(f"el pajaro vuela {metros} metros")

# piolin = Pajaro(3, "Amarillo")

# piolin.nacer()
# # lo sobreescribe, heredado  pero modificado
# piolin.hablar()

# piolin.volar(100)


class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print("Que tal")
#herencia multiple, primero hereda de padre y luego de madre, toma lo
#primero cuando tienen el mismo metodo
class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()

# Method Resolution Order. orden en que se resuelve la herencia de los
# metodos
print(Nieto.__mro__)


class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Pez, Reptil, Ave, Mamifero):
    pass
     

