import csv


class LeitorCSV:
    @staticmethod
    def ler(csv_path):
        with open(csv_path) as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            dados = [linha for linha in leitor]
        return dados
