# class Pajaro():
#     pass

# # una instacia u objeto
# pajaro = Pajaro()
# otro_pajaro = Pajaro()
# print(pajaro)
# print(type(pajaro))

# print(otro_pajaro)

# ### Atributos de instacia
# class Pajaro:

#     alas = True
      # Atributo de instacia los init
#     def __init__(self, color, especie):
#         self.color = color
#         self.especie = especie

#     # def __init__(self, parametro):
#     #     self.atributo = parametro

#     def piar(self):
#         print("pio")
#         print(f"Mi color es {self.color}")

#     def volar(self, metros):
#         print(f"El pajaro ha volado {metros} metros")

# mi_pajaro = Pajaro("negro", "tucan")
# print(f"Mi parajaro es de color {mi_pajaro.color}")
# print(f"Mi parajaro es de especie {mi_pajaro.especie}")


# ### Atributos de clase seria alas
# print(Pajaro.alas)
# print(mi_pajaro.alas)


# piolin = Pajaro("amarillo", "canario")
# piolin.piar()
# piolin.volar(50)


## Decoradores

class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    # Metodo de instacia
    # acceden y modifican atributos del objeto
    # pueden acceder a otros metodos
    # modificar el estado de la clase

    def piar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es {self.color}")

    # metodos de clase
    # no necesitan una instacia para poder ejecutarse
    # no pueden acceder a los atributos de instancia
    # modifica atributos de clase, alas
    @classmethod
    def poner_huevo(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    # metodos estaticos
    # no midifican el estado de una instacia
    # no se puede cambiar los atributos de la instancia
    # no acceden a tributos de clase ni de instacia
    @staticmethod
    def mirar():
        print("El pajaro mira")




# piolin = Pajaro("amarillo", "canario")
# piolin.volar(50)
# piolin.pintar_negro()

# piolin.alas = False
# print(piolin.alas)

# metodo de clase
Pajaro.poner_huevo(4)
Pajaro.piar()

# metodo estatico
Pajaro.mirar()