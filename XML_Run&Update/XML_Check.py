
import logging
import xml.etree.ElementTree as ET

#Util
def check_attributes_in_xml(xml_file, attributes_values):
    """ Check if any element in the XML file has the specified attributes with the given values """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    def check_element(elem):
        """ Recursively check each element for all attribute-value pairs """
        for attr, val in attributes_values:
            if elem.attrib.get(attr) == val:
                return True
        return any(check_element(child) for child in elem)

    return check_element(root)


#Run
def run_xml_attribute():
    """ Run a test to check for specific attributes in an XML file """
    # Path to your XML file
    xml_file_path = r"C:\Users\asekerci\Desktop\automation_test\FILE_NAME.xml"

    # List of attribute-value pairs to check
    attributes_to_check = [
        ('useAlignment', 'true'),
        ('type', 'baseline'),
        ('sid', '1')
    ]
    logging.info('test ')
    # Use the utility function to check the XML file for each attribute-value pair
    for attribute, value in attributes_to_check:
        attribute_exists = check_attributes_in_xml(xml_file_path, [(attribute, value)])
        assert attribute_exists, f"Attribute {attribute} with value {value} not found in the XML file."
        print(f"Test passed: Attribute {attribute} with value {value} found in the XML file.")
        print(attribute)

# Run the test





run_xml_attribute()
