import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(csv_path):
        if not csv_path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        try:
            with open(csv_path) as csv_data:
                reader = csv.DictReader(csv_data)
                data = [line for line in reader]
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        return data
