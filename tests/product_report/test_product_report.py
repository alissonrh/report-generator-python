from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_do_produto = "Suco de Laranja"
    nome_da_empresa = "Suq"
    data_de_fabricacao = "01/02/2023"
    data_de_validade = "10/02/2023"
    numero_de_serie = "123456789"
    instrucoes_de_armazenamento = "Consumir em até 3 dias após aberto"
    product_print = (
        "O produto Suco de Laranja fabricado em 01/02/2023 por Suq "
        "com validade até 10/02/2023 "
        "precisa ser armazenado Consumir em até 3 dias após aberto."
    )

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )
    assert product.__repr__() == product_print
