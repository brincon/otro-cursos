# ejercicio opcional:crear una clase persona y a la clase cuenta agregarle una persona. 

class Persona:
    #init es el constructor de la clase, init con los guiones es sintaxis de python
    def __init__(self, nombre, edad, telefono, correo, direccion, nacionalidad, profesion, documento): #init es el constructor a la clase 
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.nacionalidad = nacionalidad
        self.profesion = profesion
        self.documento = documento
        # son atributos
