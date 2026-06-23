from order import calculate_total, apply_discount


def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 60


def test_calculate_total_lista_vazia():
    assert calculate_total([]) == 0

def test_apply_discount():
    assert apply_discount(100, 10) == 90