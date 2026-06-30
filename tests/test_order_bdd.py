from pytest_bdd import scenarios, given, when, then, parsers
from order import calculate_total

scenarios("features/order_total.feature")


@given(parsers.parse("que o pedido possui os itens {itens}"), target_fixture="itens_pedido")
def pedido_com_varios_itens(itens):
    texto = itens.replace(" e ", ", ")
    return [int(v.strip()) for v in texto.split(",")]


@given(parsers.parse("que o pedido possui apenas o item {valor:d}"), target_fixture="itens_pedido")
def pedido_com_um_item(valor):
    return [valor]


@when("o sistema calcula o valor total", target_fixture="resultado")
def calcula_total(itens_pedido):
    return calculate_total(itens_pedido)


@then(parsers.parse("o resultado deve ser {esperado:d}"))
def verifica_resultado(resultado, esperado):
    assert resultado == esperado