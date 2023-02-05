from requests import get
import xml.etree.ElementTree as ET
import os


class Xml_adapter:

    def __init__(self, config: str = 'config.xml'):
        self.master = 'Config'
        self.config_name = config
        check_file = os.path.isfile(self.config_name)
        if check_file:
            return
        elif not check_file:
            data_xml = ET.Element(self.master)
            b_xml = ET.ElementTree(data_xml)
            b_xml.write(open(self.config_name, 'wb'), encoding='UTF-8', xml_declaration=True)

    def read_xml(self, subElement_tag: str = None):
        if subElement_tag is not None:
            root = ET.parse(self.config_name).getroot()
            return root.find(subElement_tag)

    def add_to_xml(self, subElement_tag: str = None, subElement_text: str = None):
        root = ET.parse(self.config_name).getroot()
        newElement = ET.Element(self.master)
        newSubElement = ET.SubElement(newElement, subElement_tag)
        newSubElement.text = subElement_text
        root.insert(0, newSubElement)
        tree = ET.ElementTree(root)
        tree.write(open(self.config_name, 'wb'), encoding='UTF-8', xml_declaration=True)


if __name__ == '__main__':
    pass

