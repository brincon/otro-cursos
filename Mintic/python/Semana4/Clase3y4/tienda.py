from producto import Producto
#1. hace una clase que se llame Tienda
#2. atributos
# nombre
# pagina web
#direccion
# lista productos

#1
class Tienda:
    #2
    def __init__(self, nombre, paginaWeb, direccion, rangoDescuento): #init es el constructor a la clase 
        self.nombre = nombre
        self.paginaWeb = paginaWeb
        self.direccion = direccion
        self.listaDeProductos = []
        self.totalVentas = 0
        self.listaVendedores = []
        self.listaClientes = []
        self.rangoDescuento = rangoDescuento
        
    #5 crar un metodo (agregarProducto) en la clase tienda para agregar un nuevo producto
    def agregarProducto(self, productoAAgregar):
        self.listaDeProductos.append(productoAAgregar)
        print("Producto agregado")
    #8 # hacer un metodo en la clase tienda para imprimir el nombre y el inventario de cada uno 
    # de los productos de la tienda
    def impresion(self):
        for producto in self.listaDeProductos:
            print("Nombre: ", producto.nombre)
            print("Inventario: ", producto.inventario)
            print("_________________")

    def buscarProductoPorNombre(self, nombreProductoABuscar):
        for producto in self.listaDeProductos:
            if producto.nombre == nombreProductoABuscar:
                return producto
            return False
            #     if producto.inventario < cantidadProducto:
            #         print("No hay inventario")
            #     else:
            #         totalVenta = cantidadProducto * producto.precio
            #         producto.inventario = producto.inventario - cantidadProducto
            #         print("El total de la venta es: ", totalVenta)
            #         print("Venta exitosa")
            # else:
            #     print("No hay inventario")
    
    def mostrarTotalDeVentas(self):
        print(f"El total de las ventas acumuladas es de: ${self.totalVentas} pesos")
    
    def agregarVendedor(self, vendedor):
        self.listaVendedores.append(vendedor)

    def buscarVendedorPorDocumento(self, documento):
        for vendedor in self.listaVendedores:
            if vendedor.documento == documento:
                return vendedor
            return False

    def agregarCliente(self, cliente):
        self.listaClientes.append(cliente)

    def buscarClientePorDocumento(self, documento):
        for cliente in self.listaClientes:
            if cliente.documento == documento:
                return cliente
            return False


    

