from requests import get
import xml.etree.ElementTree as ET
import os


class Xml_adapter:

    def __init__(self, config: str = 'config.xml'):
        self.master = 'Config'
        self.config_name = config
        check_file = os.path.isfile(self.config_name)
        #TODO: expect file is exist
        if check_file:
            return
        elif not check_file:
            data_xml = ET.Element(self.master)
            b_xml = ET.tostring(data_xml)
            with open(self.config_name, 'wb') as f:
                f.write(b_xml)

    def read_xml(self):
        root = ET.parse(self.config_name).getroot()

    def add_to_xml(self, sub_tag: str = None, sub_text: str = None):
        root = ET.parse(self.config_name).getroot()
        newElement = ET.Element(self.master)
        newSubElement = ET.SubElement(newElement, sub_tag)
        newSubElement.text = sub_text
        root.insert(0, newSubElement)
        tree = ET.ElementTree(root)
        tree.write(open(self.config_name, 'w'), encoding='unicode')


if __name__ == '__main__':
    a = Xml_adapter()
    b = input()
    a.add_to_xml(sub_text='https://google.pl/', sub_tag='Google')
    c = input()
    a.add_to_xml(sub_tag='Zooplus', sub_text='https://zooplus.pl/')
    c = input()