from model.factura import Factura

class Cliente:
    def __init__(self, nombre: str, cedula: str):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__facturas = []
        
    def get_nombre(self):
        return self.__nombre
    
    def get_cedula(self):
        return self.__cedula
    
    def get_facturas(self):
        return self.__facturas
    
    def adicionar_factura(self, factura_nueva: Factura):
        self.__facturas.append(factura_nueva)