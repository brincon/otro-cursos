class Persona:
    def __init__(self, nombre, documento, correo): #init es el constructor a la clase 
        self.nombre = nombre
        self.documento = documento
        self.correo = correo

    # esto es lo que imprime
    def __str__(self):
        return self.nombre + "  " + self.documento


persona1 = Persona("Daniel", "123", "dfs")
persona2 = Persona("Susada", "456", "sdf")

print(persona1)
print(persona2)