class Cliente:

    #Constructor de la clase
    def __init__(self, nombre, correo, edad, telefono):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.telefono = telefono

    def comprar(self, producto, tienda):
        self.producto = producto
        self.tienda = tienda  

    def puntos(self, acumulado):
        self.acumulado = acumulado

    def __str__(self):
        return f"Nombre: {self.nombre} \nCorreo: {self.correo} \nEdad: {self.edad} \nTelefono: {self.telefono} \nEl cliente ha comprado: {self.producto} \nHa comprado en la tienda: {self.tienda} \nHa acumulado en sus compras {self.acumulado} puntos"
    