from collections import Counter
from typing import List, Dict
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(reports: List[Dict]):
        simple_report = SimpleReport.generate(reports)

        stocked_products = Counter(
            [report["nome_da_empresa"] for report in reports]
        )
        stocked_products_str = ""
        for company, stock in stocked_products.items():
            stocked_products_str += f"- {company}: {stock}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{stocked_products_str}"
        )
