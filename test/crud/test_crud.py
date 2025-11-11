from model.cliente import Cliente
from model.factura import Factura
from model.producto import Antibiotico, Fertilizante, ControlPlaga
from crud.crear import crear_cliente, crear_factura, crear_antibiotico, crear_fertilizante, crear_control_plaga 
from datetime import datetime

def test_crear_cliente():
    nombre = "Isabella"
    cedula = "1116435182"
    cliente = crear_cliente(nombre, cedula)
    assert cliente.get_cedula() == cedula
   
def test_crear_factura():
    nombre = "Isabella"
    cedula = "1116435182"
    cliente = crear_cliente(nombre, cedula)
    factura = crear_factura(cedula)
    assert cliente.get_facturas()[0] == factura
    
def test_crear_antibiotico():
    nombre = "Sana Colita de rana"
    precio = 30500
    dosis = 400
    tipoAnimal = "Bovino"
    antibiotico = crear_antibiotico(nombre, precio, dosis, tipoAnimal)
    assert antibiotico.get_tipoAnimal() == tipoAnimal
    
def test_crear_fertilizante():
    nombre = "Crecer crecer"
    precio = 55000
    ICA = "ICA 3-896"
    frecuencia = 8
    ultimaAplicacion = datetime(2023,12, 10)
    fertilizante = crear_fertilizante(nombre, precio, ICA, frecuencia, ultimaAplicacion)
    assert fertilizante.get_ultimaAplicacion() == ultimaAplicacion
    
def test_crear_control_plaga():
    nombre = "Bye bye plaga"
    precio = 200000
    ICA = "ICA 2-896"
    frecuencia = 5
    periodoCarencia = 20
    control_plaga =crear_control_plaga(nombre, precio, ICA, frecuencia, periodoCarencia)
    assert control_plaga.get_periodoCarencia() == periodoCarencia
    
    
    
    
    