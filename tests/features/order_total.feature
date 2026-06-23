Feature: Calculo do total do pedido

  Scenario: Somar os valores dos itens
    Given que o pedido possui os itens 10, 20 e 30
    When o sistema calcula o valor total
    Then o resultado deve ser 60

  Scenario: Pedido com apenas um item
    Given que o pedido possui apenas o item 45
    When o sistema calcula o valor total
    Then o resultado deve ser 45