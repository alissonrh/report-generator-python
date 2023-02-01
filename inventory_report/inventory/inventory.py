import os
from inventory_report.importer.csv_importer import LeitorCSV
from inventory_report.importer.json_importer import LeitorJSON
from inventory_report.importer.xml_importer import LeitorXML
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        _, extensao = os.path.splitext(path)
        tipo_arquivo = extensao[1:].lower()
        reports: list
        if tipo_arquivo == "csv":
            reports = LeitorCSV.ler(path)
        elif tipo_arquivo == "xml":
            reports = LeitorXML.ler(path)
        elif tipo_arquivo == "json":
            reports = LeitorJSON.ler(path)
        else:
            raise ValueError(f"Tipo de arquivo {tipo_arquivo} não suportado.")
        if report_type == "simples":
            return SimpleReport.generate(reports)
        return CompleteReport.generate(reports)
