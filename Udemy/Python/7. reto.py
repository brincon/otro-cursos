class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    def __str__(self):
        return f"""
                    Cliente: {self.nombre} {self.apellido} 
                    Balance de cuenta: {self.numero_cuenta}, ${self.balance}
                    """
    
    def depositar(self):
        depositar = int(input("Por favor ingrese el monto que quiere depositar en su cuenta: "))
        self.balance = self.balance + int(depositar)
        print("Deposito aceptado")

    def retirar(self):
        retirar = int(input("Por favor ingrese el monto que quiere retirar de su cuenta: "))
        if self.balance < int(retirar):
            print("\nFondos insuficientes\n")
        else:
            self.balance = self.balance - int(retirar)
            print("Retiro aceptado")


def crear_cliente():
    nombre = input("Por favor ingrese su nombre: ")
    apellido = input("Por favor ingrese su apellido: ")
    numero_cuenta = input("Por favor ingrese su numero de cuenta: ")
    cliente = Cliente(nombre, apellido, numero_cuenta)
    return cliente

def inicio ():
    print("**" * 46)
    print("**" *20 + " Bienvenido " + "**" *20)
    print("**" * 46)
    cliente = crear_cliente()
    print(cliente)
    opciones = True
    while opciones:
        opciones = input("""
                Por favor ingrese una opción:
                1. Depositos
                2. Retiros
                3. Salir
                """)
        
        if opciones == "1":
            cliente.depositar()
            print(str(cliente))
        
        elif opciones == "2":
            cliente.retirar()
            print(str(cliente))

        else:
            opciones = False

    print("Gracias por operar")

inicio()
