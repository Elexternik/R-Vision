import xml.etree.ElementTree as ET

def parse_oval_objects(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    objects = []

    namespace = {'red-def': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux'}

    for obj in root.findall('.//red-def:rpminfo_object', namespace):
        obj_id = obj.get('id')
        obj_version = obj.get('version')
        name_elem = obj.find('red-def:name', namespace)
        name = name_elem.text if name_elem is not None else 'N/A'
        
        objects.append({
            'type': 'rpminfo_object',
            'id': obj_id,
            'version': obj_version,
            'name': name
        })
    
    for obj in root.findall('.//red-def:rpmverifyfile_object', namespace):
        obj_id = obj.get('id')
        obj_version = obj.get('version')
        filepath_elem = obj.find('red-def:filepath', namespace)
        filepath = filepath_elem.text if filepath_elem is not None else 'N/A'
        
        objects.append({
            'type': 'rpmverifyfile_object',
            'id': obj_id,
            'version': obj_version,
            'filepath': filepath
        })

    return objects
separator = "--------------------------------------------------------------------"
def save_objects_to_file(objects, output_file):
    with open(output_file, 'w') as file:
        for obj in objects:
            if obj['type'] == 'rpminfo_object':
                file.write(f"Type: rpminfo_object\nID: {obj['id']}\nVersion: {obj['version']}\nName: {obj['name']}\n{separator}\n")
            elif obj['type'] == 'rpmverifyfile_object':
                file.write(f"Type: rpmverifyfile_object\nID: {obj['id']}\nVersion: {obj['version']}\nFilePath: {obj['filepath']}\n{separator}\n")


input_file = 'rhel-8.oval.xml'
output_file = 'parsed_objects.txt'

objects = parse_oval_objects(input_file)
save_objects_to_file(objects, output_file)

