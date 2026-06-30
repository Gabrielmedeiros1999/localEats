def calculate_total(items: list[float]) -> float:
    """Calcula e retorna o valor total de uma lista de itens.

    Args:
        items: Lista de valores (float) dos itens do pedido.

    Returns:
        A soma de todos os valores da lista.
    """
    return sum(items)


def apply_discount(total: float, discount_percent: float) -> float:
    return total - (total * discount_percent / 100)
