from model.factura import Factura
from model.cliente import Cliente

def test_facturas():
    cliente = Cliente("Pedro","1020775867")
    factura = Factura()
    cliente.adicionar_factura(factura)
    
    assert len(cliente.get_facturas()) == 1