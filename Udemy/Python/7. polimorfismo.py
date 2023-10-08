class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice bee")

vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

vaca1.hablar()
oveja1.hablar()

# puede ejecutar metodos que tengan el mismo nombre. Son clases diferentes
# pero que tienen el mismo metodo, hablar
animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()

# Ahora con una funcion
def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)


# class Mago():
#     def atacar(self):
#         print("Ataque mágico")

# class Arquero():
#     def atacar(self):
#         print("Lanzamiento de flecha")

# class Samurai():
#     def atacar(self):
#         print("Ataque con katana")
        
# mago = Mago()
# arquero = Arquero()
# samurai = Samurai()

# lista = [mago, arquero, samurai]

# for personaje in lista:
#     personaje.atacar()