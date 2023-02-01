from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter


def test_decorar_relatorio():
    colored_phrases = [
        "\033[32mData de fabricação mais antiga:\033[0m",
        "\033[32mData de validade mais próxima:\033[0m",
        "\033[32mEmpresa com mais produtos:\033[0m",
        "\033[36m2020-09-06\033[0m",
        "\033[36m2023-09-17\033[0m",
        "\033[31mTarget Corporation\033[0m",
    ]
    path = "inventory_report/data/inventory.csv"
    reports = CsvImporter.import_data(path)
    colored_report = ColoredReport(SimpleReport)
    report_list = colored_report.generate(reports)
    for phrase in colored_phrases:
        assert phrase in report_list
