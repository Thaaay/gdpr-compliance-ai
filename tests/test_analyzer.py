
from src.analyzer import GDPRScanner

def test_scanner_init():
    # Este teste apenas verifica se a classe pode ser instanciada
    scanner = GDPRScanner()
    assert scanner is not None