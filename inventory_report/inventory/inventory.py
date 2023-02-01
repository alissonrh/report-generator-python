import os
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        # o método os.path.splitext separa o nome do arquivo do
        # sufixo (extensão), e a extensão é convertida para minúsculas para
        # evitar problemas com maiúsculas/minúsculas.
        _, extension = os.path.splitext(path)
        file_type = extension[1:].lower()
        reports: list
        if file_type == "csv":
            reports = CsvImporter.import_data(path)
        elif file_type == "xml":
            reports = XmlImporter.import_data(path)
        elif file_type == "json":
            reports = JsonImporter.import_data(path)
        else:
            raise ValueError(f"File type {file_type} not supported.")
        if report_type == "simples":
            return SimpleReport.generate(reports)
        return CompleteReport.generate(reports)
