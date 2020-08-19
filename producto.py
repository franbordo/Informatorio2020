class Producto:
    def __init__(self, nombre, precio, precios_cuidados=0, primera_neceisadad=0):
            self.nombre= nombre
            self.precio= precio
            self.precios_cuidados= precios_cuidados
            self.primera_neceisadad= primera_neceisadad
    def calcular_precio(self):
        if (self.primera_neceisadad==1):
            return self.precio*0.9
        return self.precio

