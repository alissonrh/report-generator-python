from collections import Counter
from typing import List, Dict
from inventory_report.reports.simple_report import SimpleReport

rep = [
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 2,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "of Nature",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 3,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Forces",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
]


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(reports: List[Dict]):
        simple_report = SimpleReport.generate(reports)

        products_couter = Counter(
            [report["nome_da_empresa"] for report in reports]
        )
        stocked_products = ""
        for company, stock in products_couter.items():
            stocked_products += f"- {company}: {stock}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{stocked_products}"
        )


print(CompleteReport.generate(rep))
