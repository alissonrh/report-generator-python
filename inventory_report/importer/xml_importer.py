import xml.etree.ElementTree as ET


class LeitorXML:
    @staticmethod
    def ler(xml_path):
        with open(xml_path) as arquivo_xml:
            xml_tree = ET.parse(arquivo_xml)
            root = xml_tree.getroot()
            dados = []
            for child in root:
                linha = {}
                for elem in child:
                    linha[elem.tag] = elem.text
                dados.append(linha)
        return dados
