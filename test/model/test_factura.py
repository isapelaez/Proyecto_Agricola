from model.factura import Factura
from model.producto import Producto


def test_get_fecha():
    factura = Factura()
    
    assert factura.get_fecha() is not None

def test_get_productos():
    factura = Factura()
    factura.adicionar_producto(Producto("dummy", 1))
    
    assert len(factura.get_productos()) == 1