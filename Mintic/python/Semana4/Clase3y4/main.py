from tienda import Tienda
from producto import Producto
from vendedor import Vendedor
from cliente import Cliente
#3
nombreTienda = str(input("Bienvenido. Ingrese el nombre de la tienda: "))
paginaWeb = str(input("Ingrese la página web de la tienda: "))
direccion = str(input("Ingrese la dirección de la tienda: "))
tienda = Tienda(nombreTienda, paginaWeb, direccion, 80000)

#6 crear manualmente un producto y agregarlo a la lista de productos de la tienda
# zapatos = Producto("zapatos", 50000)
# tienda.agregarProducto(zapatos)
# print(tienda.listaDeProductos)

# 7 hacer un while True, pedirle al usuario un input par aque el usuario ingrese
# el comando "NP" que cree un nuevo producto en la tienda

vendedor = Vendedor("Daniel", "123", "dsl@c.com", "1233", 500000, "EMP001")
while True:
    instrucciones = """
    Bienvenido, 
    Ingrese NP para crear un nuevo producto 
    I para imprimir los productos e inventario, 
    V para ejecutar una venta
    TV para ver el total de ventas  
    NV para crear un nuevo vendedor
    NC para crear un nuevo cliente
    """
    operacion = input(instrucciones).upper()
    if operacion == "NP":
        nombreProducto = input("Por favor ingrese el nombre del producto: ")
        precioProducto = int(input("Ingrese el valor del producto: "))
        productoCreado = Producto(nombreProducto, precioProducto)
        tienda.agregarProducto(productoCreado)
        #print(tienda.listaDeProductos)
    elif operacion == "I":
        tienda.impresion()
    elif operacion == "V":
        #12: buscar un vendedor
        docVendedor = input("Por favor ingrese el documento del vendedor: ")
        vendedorEncontrado = tienda.buscarVendedorPorDocumento(docVendedor)
        
        #13: buscar un cliente
        docCliente = input("Por favor ingrese el documento del cliente: ")
        clienteEncontrado = tienda.buscarClientePorDocumento(docCliente)

        nombreProducto = input("Ingrese el nombre del producto que quiere comprar: ")
        productoEncontrado = tienda.buscarProductoPorNombre(nombreProducto)
        if not productoEncontrado:
            print("El producto no fue encontrado")
        elif not vendedorEncontrado:
            print("El vendedor no fue encontrado")
        elif not clienteEncontrado:
            print("El cliente no fue encontrado")
        else:
            cantidadAComprar = int(input("Ingrese la cantidad a comprar: "))
            if productoEncontrado.inventario >= cantidadAComprar:
                total = productoEncontrado.precio * cantidadAComprar
                print(f"Venta exitosa, el total de la venta es: ${total} pesos") 
                productoEncontrado.inventario = productoEncontrado.inventario - cantidadAComprar
                tienda.totalVentas = tienda.totalVentas + total
                
                #12: acumular totales en el vendedor
                vendedorEncontrado.acumular(total)
                vendedorEncontrado.revisarObjetivo()
                print(f"El total de las ventas realizadas en el día es de: ${tienda.totalVentas} pesos")
            
            #12: acumular totales en el cliente
                clienteEncontrado.acumular(total)
                aplicaDescuento = clienteEncontrado.revisarDescuento(tienda.rangoDescuento)
                if aplicaDescuento:
                    total= total * 90/100
                    print("Obtuviste un descuento del 10%")
                    print(f"Lo que debes pagar es {total}")
                
                print(f"El total de ventas realizadas en el día es de: ${tienda.totalVentas} pesos")

            
            else:
                print("No hay suficiente inventario de la referencia que sea comprar")
    elif operacion == "TV":
        tienda.mostrarTotalDeVentas()
    elif operacion == "NV":
        nombre = input("Ingrese el nombre del nuevo vendedor: ")
        telefono = input("Ingrese el telefono del nuevo vendedor: ")
        correo = input("Ingrese el correo del nuevo del vendedor: ")
        documento = input("Ingrese el documento del nuevo vendedor: ")
        objetivo = int(input("Ingrese el objetivo de ventas del nuevo vendedor: "))
        docEmpresarial = input("Ingrese el docEmpresarial del nuevo vendedor: ")
        nuevoVendedor = Vendedor(nombre, telefono, correo, documento, objetivo, docEmpresarial)
        tienda.agregarVendedor(nuevoVendedor)
    elif operacion == "NC":
        nombre = input("Ingrese el nombre del nuevo cliente: ")
        telefono = input("Ingrese el telefono del nuevo cliente: ")
        correo = input("Ingrese el correo del nuevo del cliente: ")
        documento = input("Ingrese el documento del nuevo cliente: ")
        direccion = input("Ingrese la direccion de envío: ")
        correoFacturacion = input("Ingrese el correo de facturacion: ")
        nuevoCliente = Cliente(nombre, telefono, correo, documento, direccion, correoFacturacion)
        tienda.agregarCliente(nuevoCliente)


#9 hacer una funcion de venta en la clase tienda, es una funcion que recibe 
# el nombre del producto y la cantidad de elementos que se quiere comprar
# si hay inventario, calcular el total de la venta (cantidad * precio) y mostrar "venta exitosa"
# si no hay inventario suficiente mostrar un mensaje que diag aque no hay unidades

