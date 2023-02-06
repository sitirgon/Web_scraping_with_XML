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
            b_xml.write(self.config_name, encoding='UTF-8', xml_declaration=True)

    def read_xml(self, sub_element_tag: str = None):
        root = et.parse(self.config_name).getroot()
        if sub_element_tag is not None:
            return root.findall(sub_element_tag)
        elif sub_element_tag is None:
            tree = et.ElementTree(root)
            return [(i.tag, i.text)
                    for i in tree.iter()
                    if i.text is not None]

    def add_to_xml(self, sub_element_tag: str = None, sub_element_text: str = None):
        root = et.parse(self.config_name).getroot()
        new_element = et.Element(self.master)
        new_sub_element = et.SubElement(new_element, sub_element_tag)
        new_sub_element.text = sub_element_text
        root.insert(0, new_sub_element)
        tree = et.ElementTree(root)
        tree.write(self.config_name, encoding='UTF-8', xml_declaration=True)

    def remove_from_xml(self, sub_element_tag: str = None):
        root = et.parse(self.config_name).getroot()
        print(root.findall(sub_element_tag))
        if root.findall(sub_element_tag):
            root.remove(root.find(sub_element_tag))
            tree = et.ElementTree(root)
            tree.write(self.config_name, encoding='UTF-8', xml_declaration=True)
        elif not root.findall(sub_element_tag):
            return 0

