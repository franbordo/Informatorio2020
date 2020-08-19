from producto import Producto
class Supermercado:
    def __init__(self, nombre, direccion, catalogo=[]):
        self.nombre=nombre
        self.direccion=direccion
        self.catalogo=catalogo
    def __str__(self):
        return f"Nombre\t {self.catalogo}\n" \

               
    def cargarCatalogo(self, nombre, precio, precios_cuidados=0, primera_neceisadad=0):
        catalogo=Producto(nombre, precio, precios_cuidados, primera_neceisadad)
        self.catalogo.append(catalogo)
    def stock(self):
        return len(self.catalogo)
    def sumPrecio(self):
        suma=0
        for i in self.catalogo:
            suma+=i.calcular_precio

    
print("Hola mundo, que cambiado estás") 