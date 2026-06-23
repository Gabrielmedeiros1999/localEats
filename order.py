def calculate_total(items: list[float]) -> float:
    """
    Calcula e retorna o valor total de uma lista de itens.

    Args:
        items: Lista de valores dos itens.

    Returns:
        Soma dos valores.
    """
    return sum(items)

def apply_discount(total: float, discount_percent: float) -> float:
    return total - (total * discount_percent / 100)