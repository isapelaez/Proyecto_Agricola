from datetime import datetime
from model.producto import Producto

class Factura:
    def __init__(self):
        self.__fecha = datetime.now()
        self.__total = 0
        self.__productos = []
    
    def get_fecha(self):
        return self.__fecha
    
    def get_productos(self):
        return self.__productos
    
    def get_total(self):
        return self.__total
    
    def adicionar_producto(self, productoNuevo: Producto):
        self.__productos.append(productoNuevo)
        self.__total += productoNuevo.get_precio()
        
    
    