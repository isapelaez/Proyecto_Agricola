from datetime import datetime

class Producto:
    def __init__(self, nombre: str, precio: float):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio

    def set_precio(self):
        return self.__precio

class Antibiotico(Producto):
    def __init__(self, nombre: str, precio: float, dosis: float, tipoAnimal: str):
        super().__init__(nombre, precio)
        self.__dosis = dosis
        self.__tipoAnimal = tipoAnimal
        
    def get_dosis(self):
        return self.__dosis
    
    def get_tipoAnimal(self):
        return self.__tipoAnimal

class ProductoControl(Producto):
    def __init__(self, nombre: str, precio: float, ICA: str, frecuencia: int):
        super().__init__(nombre, precio)
        self.__ICA = ICA
        self.__frecuencia = frecuencia
   
    def get_ICA(self):
        return self.__ICA
    
    def get_frecuencia(self):
        return self.__frecuencia   

class Fertilizante(ProductoControl):
    def __init__(self, nombre: str, precio: float, ICA: str, frecuencia: int, ultimaAplicacion: datetime):
        super().__init__(nombre, precio, ICA, frecuencia)
        self.__ultimaAplicacion = ultimaAplicacion
        
    def get_ultimaAplicacion(self):
        return self.__ultimaAplicacion

class ControlPlaga(ProductoControl):
    def __init__(self, nombre: str, precio: float, ICA: str, frecuencia: int, periodoCarencia: int):
        super().__init__(nombre, precio, ICA, frecuencia)
        self.__periodoCarencia = periodoCarencia
        
    def get_periodoCarencia(self):
        return self.__periodoCarencia