import pytest
from src.utils import calculate_cart_total

def test_total_valores_validos():
    itens = [{'name': 'A', 'price': 10.0, 'qty': 2}]
    total = calculate_cart_total(itens, discount=0.1, tax_rate=0.2)
    assert total == 21.6

def test_total_lista_vazia():
    assert calculate_cart_total([], 0, 0) == 0.0

def test_total_valor_negativo():
    itens = [{'name': 'A', 'price': -1.0, 'qty': 1}]
    with pytest.raises(ValueError):
        calculate_cart_total(itens)
