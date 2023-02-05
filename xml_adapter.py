from os import path
import xml.etree.ElementTree as et


class XmlAdapter:

    def __init__(self):
        self.master = 'Config'
        self.config_name = 'config.xml'
        check_file = path.isfile(self.config_name)
        if check_file:
            return
        elif not check_file:
            data_xml = et.Element(self.master)
            b_xml = et.ElementTree(data_xml)
            b_xml.write(open(self.config_name, 'wb'), encoding='UTF-8', xml_declaration=True)

    def read_xml(self, sub_element_tag: str = None):
        if sub_element_tag is not None:
            root = et.parse(self.config_name).getroot()
            return root.find(sub_element_tag)

    def add_to_xml(self, sub_element_tag: str = None, sub_element_text: str = None):
        root = et.parse(self.config_name).getroot()
        new_element = et.Element(self.master)
        new_sub_element = et.SubElement(new_element, sub_element_tag)
        new_sub_element.text = sub_element_text
        root.insert(0, new_sub_element)
        tree = et.ElementTree(root)
        tree.write(open(self.config_name, 'wb'), encoding='UTF-8', xml_declaration=True)