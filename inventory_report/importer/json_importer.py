import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(json_path):
        if not json_path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(json_path) as arquivo_json:
            data = json.load(arquivo_json)
        return data
