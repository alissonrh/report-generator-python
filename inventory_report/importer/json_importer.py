import json


class LeitorJSON:
    @staticmethod
    def ler(json_path):
        with open(json_path) as arquivo_json:
            dados = json.load(arquivo_json)
        return dados
