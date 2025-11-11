from model.cliente import Cliente
from model.factura import Factura
from model.producto import Antibiotico, Fertilizante, ControlPlaga
from datetime import datetime

clientes: dict[str, Cliente] = {}

def crear_cliente(nombre: str, cedula: str):
    cliente = Cliente(nombre, cedula)
    clientes[cedula] = cliente
    return cliente
    
def crear_factura(cedula: str):
    factura = Factura()
    clientes[cedula].adicionar_factura(factura)
    return factura
    
def crear_antibiotico(nombre: str, precio: float, dosis: int, tipoAnimal: str):
    antibiotico = Antibiotico(nombre, precio, dosis, tipoAnimal)
    return antibiotico
    
def crear_fertilizante(nombre: str, precio: float, ICA: str, frecuencia: int, ultimaAplicacion: datetime):
    fertilizante = Fertilizante(nombre, precio, ICA, frecuencia, ultimaAplicacion)
    return fertilizante
    
def crear_control_plaga(nombre: str, precio: float, ICA: str, frecuencia: int, periodoCarencia: int):
    control_plaga = ControlPlaga(nombre, precio, ICA, frecuencia, periodoCarencia)
    return control_plaga
    
def buscar_cliente(cedula: str):
    if cedula in clientes:
        return clientes[cedula]
    else:
        return None
