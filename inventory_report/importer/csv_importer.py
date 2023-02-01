import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(csv_path):
        if not csv_path.endswith(".xml"):
            raise ValueError("Invalid file")

        with open(csv_path) as csv_data:
            reader = csv.DictReader(csv_data)
            data = [line for line in reader]
        return data
