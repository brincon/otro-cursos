import random
from persona import Persona


#hacer una clase que se llame cuentaBancaria
#atributos:
# número de la cuenta -> es un aleatorio entre 1.000 y 10.000
# saldo
#metodos
# retirar
# depositar
# ejercicio: agregar condicion para que saque error si el saldo es negativo

# ejercicio: cobrar una comisión del 4 por 1000 cuando el monto de la consignación sea mayor a 10.000
# ejercicio opcional: crear una lista de cuentas y agregar la posibilidad de crear una cuenta nueva o eliminar una cuenta
# cuando se vaya a retirar o consignar, se debe ingresar el número de la cuenta

# ejercicio opcional: crear una clase persona y a la clase cuenta agregarle una persona. 
# Hay que construir una lista de personas. Si la persona no existe se debe crear.

# write a pyrhon class named circle construted by a radius and two methods which will
# compute the area and perimeter of a circle

# 2. write a python class named rectagle constructed a by leng and width and a method which will
# compute the area of a rentangle

# 3. crear una clase inventario, tenga un codigo de referencia, unas unidades y un método para
# retirar y agregar unidades a la referencia. Debe tener un método para consultar las unidades restantes

# el init solo debe aparecer una vez 
class CuentaBancaria:
    def __init__(self,saldoInicial,personaPropietaria):
        self.numeroCuenta = random.randint(1000,10000)
        self.saldo = saldoInicial
        self.propietario = personaPropietaria

    def retirar (self, monto):
        if monto > self.saldo:
            print("Su saldo es insuficiente")
        else:
         self.saldo = self.saldo - monto
         print("Retiro Exitoso")
    
    def consultarSaldo(self):
        print("Cuenta: ", self.numeroCuenta)
        print("Saldo: ", self.saldo)
        print("___________________")
    
    def consignar(self, monto):
        if monto > 10000:
            comision = monto * 4 / 1000
            monto = monto - comision
            print("La comisión por la consignación es de: ", comision)
            self.saldo = self.saldo + monto
        else:
            self.saldo = self.saldo + monto

# cuenta1 = CuentaBancaria(1000)
# cuenta1.consultarSaldo()
# cuenta1.retirar(500)
# cuenta1.consultarSaldo()
# cuenta1.consignar(2000)
# cuenta1.consultarSaldo()

# def buscarCuentas(mensajeOperacion, listaDeCuentas):
#     #pedir el número de la cuenta al usuario
#     numCuenta = int(input(mensajeOperacion))
    #buscar la cuenta del usuario. Cuando se encuentre, imprimir el saldo
    # for cuentaIteracion in listaDeCuentas:
    #     if cuentaIteracion.numeroCuenta == numCuenta:
    #         #así sería con la opcion de lista y posición
    #         return [True, cuentaIteracion]
    # return [False]

def buscarCuentas(mensajeOperacion, listaDeCuentas):
    #pedir el número de la cuenta al usuario
    numCuentaABuscar = int(input(mensajeOperacion))
    #buscar la cuenta del usuario. Cuando se encuentre, imprimir el saldo
    for cuentaIteracion in listaDeCuentas:
        if cuentaIteracion.numeroCuenta == numCuentaABuscar:
            return cuentaIteracion
    return False

def buscarPersona(cedula,listaDePersonas):
    for persona in listaDePersonas:
        if persona.documento == cedula:
            return persona
    return False

listaDeCuentas = []
listaDePersonas = []

while True:
    operacion = input("Ingrese N para crear una nueva cuenta, S para consultar el saldo, R para retirar y C para consignar: ")
    if operacion == "N":
        saldoInicial = float(input("Bienvenido al banco XYZ. Para crear su cuenta bancaria, ingrese el saldo inicial de la cuenta: "))
        
        #por hacer:
        #1. pedirle la cédula al usuario.
        cedula  = input("Por favor ingrese su cédula: ")
        #2. buscar el usuario. Si existe, asociar la cuenta a ese usuario.
        personaEncontrada = buscarPersona(cedula,listaDePersonas)
        #3. si no existe, preguntar la info personal de la persona, crear la persona y asociar la nueva cuenta a esa persona
        if not personaEncontrada:
            #crear una nueva persona
            nuevaPersona = Persona("Daniel",48, 23434, "dsl@c.com","sfdsf","Colombiano","ingeniero","1065377193")
            listaDePersonas.append(nuevaPersona)
            #crear una nueva cuenta bancaria y asociarla a la persona recientemente creada
            nuevaCuenta = CuentaBancaria(saldoInicial, nuevaPersona)
            listaDeCuentas.append(nuevaCuenta)
        else:
            #crear una nueva cuenta bancaria y asociarla a la persona recientemente creada
            nuevaCuenta = CuentaBancaria(saldoInicial, personaEncontrada)
            listaDeCuentas.append(nuevaCuenta)
        print("Cuenta creada con éxito. El número de la cuenta es: ", nuevaCuenta.numeroCuenta)
    # elif operacion == "S":
    #     #pedir el numero de la cuenta al usuario
    #     resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta que quiere consultar: ", listaDeCuentas)
        # esta opción toma las posiciones de la lista que se obtiene en el return. Si la posicion cero es verdadero me trae
        # la cuenta de lo contrario es falso, por eso no hay necesidad de colocar otra condicion, es un verdadero o falso
        # if resultadoBusqueda[0]:
        #     cuentaEncontrada = resultadoBusqueda[1]
        #     cuentaEncontrada.consultarSaldo()
        # else:
        #     print("Cuenta no encontrada")

        # de esta forma se hace lo mismo sin posiciones, entonces si no tengo resultado de la busqueda (Falso) entonces imprina eso
        # de lo contrario a esa cuenta encontrada consulte el saldo.
    elif operacion == "S":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta que quiere consultar: ",listaDeCuentas)
        if not resultadoBusqueda:
            print("Cuenta no encontrada")
        else:
            resultadoBusqueda.consultarSaldo()
    elif operacion == "R":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta de la quiere retirar: ", listaDeCuentas)
        if not resultadoBusqueda:
            print("Cuenta no encontrada")
        else:
            monto = float(input("Ingrese el monto que quiere retirar: "))
            resultadoBusqueda.retirar(monto)
    elif operacion == "C":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta a la quiere consignar", listaDeCuentas)
        if not resultadoBusqueda:
            print("Cuenta no encontrada")
        else:
            monto = float(input("Ingrese el monto que quiere consignar: "))
            resultadoBusqueda.consignar(monto)
            print("Consignación exitosa")
    else:
        print("Operación incorrecta")