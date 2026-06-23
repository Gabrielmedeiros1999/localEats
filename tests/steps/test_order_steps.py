from pytest_bdd import given, when, then
from order import calculate_total


@given(
    "que o pedido possui os itens 10, 20 e 30",
    target_fixture="order_items"
)
def order_items():
    return [10, 20, 30]


@given(
    "que o pedido possui apenas o item 45",
    target_fixture="single_item"
)
def single_item():
    return [45]


@when(
    "o sistema calcula o valor total",
    target_fixture="total"
)
def calculate(order_items=None, single_item=None):
    items = order_items if order_items is not None else single_item
    return calculate_total(items)


@then("o resultado deve ser 60")
def check_total_60(total):
    assert total == 60


@then("o resultado deve ser 45")
def check_total_45(total):
    assert total == 45