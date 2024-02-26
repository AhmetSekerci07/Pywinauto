from lxml import etree
import hashlib


def calculate_md5_hash(file_path):
    """ Calculate the MD5 hash of a file. """
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


def update_memory_threshold_with_lxml(file_path, new_value):
    # Parse the XML file while keeping comments
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file_path, parser)
    root = tree.getroot()

    # Flag to check if update was made
    update_made = False

    # Find and update the 'ThreeD_Memory_Threshold' element
    for elem in root.iter('ThreeD_Memory_Threshold'):
        if elem.text == '500':
            elem.text = new_value
            update_made = True

    # Write the changes back to the file, preserving comments
    if update_made:
        tree.write(file_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')
        print("XML file updated successfully with lxml.")

        # Calculate and return the new MD5 hash of the updated file
        return calculate_md5_hash(file_path)
    else:
        print("No matching elements found to update.")
        return None


# Path to your XML file
xml_file_path = r'C:\Users\asekerci\Desktop\automation_test/Application Settings.xml'

# The new value you want to set
new_memory_threshold = '100000000'

# Update the XML file using lxml and get the new MD5 hash
new_md5_hash = update_memory_threshold_with_lxml(xml_file_path, new_memory_threshold)

if new_md5_hash:
    print(f"New MD5 hash of the updated XML file: {new_md5_hash}")
