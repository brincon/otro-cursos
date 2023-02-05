import random

#hacer una clase que se llame cuentaBancaria
#atributos:
# número de la cuenta -> es un aleatorio entre 1.000 y 10.000
# saldo
#metodos
# retirar
# depositar
# ejercicio: agregar condicion para que saque error si el saldo es negativo
# ejercicio: cobrar una comisión del 4 por 1000 cuando el monto de la consignación sea mayor a 10.000
# ejercicio opcional: crear una lista de cuentas y agrega rla posibilidad de crear una cuenta o eliminar una cuenta
# cuando se vaya a retirar o consignar, se debe ingresar el número de la cuenta

# ejercicio opcional:crear una clase persona y a la clase cuenta agregarle una persona. 
# Hay que construir una lista de personas. Si la persona no existe se debe crear.

# write a pyrhon class named circle construted by a radius and two methods which will
# compute the area and perimeter of a circle

# 2. write a python class named rectagle constructed a by leng and width and a method which will
# compute the area of a rentangle

# 3. crear una clase inventario, tenga un codigo de referencia, unas unidades y un método para
# retirar y agregar unidades a la referencia. Debe tener un método para consultar las unidades restantes


# el init solo debe aparecer una vez 
class CuentaBancaria:
    def __init__(self, saldoInical):
        self.numeroCuenta = random.randint(1000, 10000)
        self.saldo = saldoInical
    
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
            comision = monto*0.004
            monto = monto - comision
            print("La comisión por la consignación es de: ", comision)
            self.saldo = self.saldo + monto

# cuenta1 = CuentaBancaria(1000)
# cuenta1.consultarSaldo()
# cuenta1.retirar(500)
# cuenta1.consultarSaldo()
# cuenta1.consignar(2000)
# cuenta1.consultarSaldo()

saldoInicial = float(input("Bienvenido al banco XYZ. Para crear su cuenta bancaria, ingrese el saldo inicial de la cuenta: "))
cuenta = CuentaBancaria(saldoInicial)
while True:
    operacion = input("Ingrese S para consultar el saldo, R para retirar y C para consignar: ", cuenta.numeroCuenta)
    if operacion == "S":
        cuenta.consultarSaldo()
    elif operacion == "R":
        monto = float(input("Ingrese el monto que quiere retirar: "))
        cuenta.retirar(monto)
    elif operacion == "C":
        monto = float(input("Ingrese el monto que quiere consignar: "))
        cuenta.consignar(monto)
        print("Consignación exitosa")
    else:
        print("Operación incorrecta")
