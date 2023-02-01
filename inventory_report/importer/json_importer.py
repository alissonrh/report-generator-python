from ast import ImportFrom
import json


class JsonImporter(ImportFrom):
    @staticmethod
    def import_data(json_path):
        if not json_path.endswith(".json"):
            raise ValueError("Invalid file")

        with open(json_path) as arquivo_json:
            data = json.load(arquivo_json)
        return data
