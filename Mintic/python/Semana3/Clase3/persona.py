
class Persona:
    #init es el constructor de la clase, init con los guiones es sintaxis de python
    def __init__(self, nombre, edad, teleno, correo, direccion, nacionalidad, profesion): #init es el constructor a la clase 
        self.nombre = nombre
        self.edad = edad
        self.telefono = teleno
        self.correo = correo
        self.direccion = direccion
        self.nacionalidad = nacionalidad
        self.profesion = profesion
        # son atributos


persona1 = Persona("Daniel", 50, 3117191377, "dff@c.com", "ds", "colombiano", "ingeniero")
persona2 = Persona("Jhon", 20, 4354, "jh@d.com", "da", "ingles", "guerrero")
print(persona1.edad)
print(persona2.edad)