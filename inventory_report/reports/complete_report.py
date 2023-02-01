from collections import Counter
from typing import List, Dict
from inventory_report.reports.simple_report import SimpleReport


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
