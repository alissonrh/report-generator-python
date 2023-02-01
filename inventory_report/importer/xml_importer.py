import xml.etree.ElementTree as ET

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(xml_path):
        if not xml_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(xml_path) as arquivo_xml:
            xml_tree = ET.parse(arquivo_xml)
            root = xml_tree.getroot()
            reports = []
            for child in root:
                report_dict = {}
                for elem in child:
                    report_dict[elem.tag] = elem.text
                reports.append(report_dict)
        return reports
