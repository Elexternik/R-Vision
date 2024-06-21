import xml.etree.ElementTree as ET


tree = ET.parse('rhel-8.oval.xml')
root = tree.getroot()

with open('filterText.txt', 'w') as file:
    for elem in root.iter('{http://oval.mitre.org/XMLSchema/oval-definitions-5}definition'):
        definition_id = elem.get('id')
        def parse_criteria(criteria_element, indent=0):
            indent_str = ' ' * indent
            if criteria_element.tag.endswith('criterion'):
                comment = criteria_element.get('comment')
                test_ref = criteria_element.get('test_ref')
                return f"{indent_str}Criterion: {comment} (Test Reference: {test_ref})"
            elif criteria_element.tag.endswith('criteria'):
                operator = criteria_element.get('operator')
                result = [f"{indent_str}Criteria (Operator: {operator}):"]
                for child in criteria_element:
                    result.append(parse_criteria(child, indent + 2))
                return "\n".join(result)

        criteria_find = root.find('.//{http://oval.mitre.org/XMLSchema/oval-definitions-5}criteria')

        if criteria_find is not None:
            result_text = parse_criteria(criteria_find)
        else:
            print("Не удалось найти элемент <criteria>")
        title = elem.find('{http://oval.mitre.org/XMLSchema/oval-definitions-5}metadata/{http://oval.mitre.org/XMLSchema/oval-definitions-5}title').text
        description = elem.find('{http://oval.mitre.org/XMLSchema/oval-definitions-5}metadata/{http://oval.mitre.org/XMLSchema/oval-definitions-5}description').text
        criteria = result_text
        separator = "----------------------------------------------------------------------------------------------"
        file.write(f"Definition ID: {definition_id}\n\n\nTitle: {title}\n\n\nDescription: {description}\n\n\nCriteria: {criteria}\n\n{separator}")

