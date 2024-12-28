import csv
import json
from collections import defaultdict

# Define the function to convert the CSV data to JSON format
def build_family_tree(csv_data):
    # Create a dictionary to store family members by their IDs
    family_members = {}

    # Parse the CSV data
    for row in csv_data:
        family_members[row['id']] = {
            'id': row['id'],
            'name': row['name'],
            'nameHindi': row['nameHindi'],
            'parentId': row['parentId'],
            'children': []
        }

    # Build the family tree by linking parents and children
    for member in family_members.values():
        if member['parentId']:
            parent = family_members[member['parentId']]
            parent['children'].append(member)

    # Find the root (the person without a parent)
    root = None
    for member in family_members.values():
        if not member['parentId']:
            root = member
            break

    # Recursively build the children list with 'childId' and 'childList'
    def format_children(member):
        children = []
        for child in member['children']:
            children.append({
                'id': child['id'],
                'name': child['name'],
                'nameHindi': child['nameHindi'],
                'children': {
                    'childId': f'{child["id"]}-Kids',  # Add childId for each child node
                    'childList': format_children(child)  # Add childList for each child node
                }
            })
        return children

    # Add childId and childList for the root and its children
    def add_child_data(member):
        children = format_children(member)
        return {
            'id': member['id'],
            'name': member['name'],
            'nameHindi': member['nameHindi'],
            'children': {
                'childId': f'{member["id"]}-Kids',  # Add childId for the current node
                'childList': children               # Add childList for the current node
            }
        }

    # Apply to the root and its descendants
    family_tree = add_child_data(root)

    return family_tree

# Read the CSV file
with open('ModaniFamily.csv', mode='r', encoding='utf-8-sig') as file:
    csv_reader = csv.DictReader(file)
    csv_data = [row for row in csv_reader]

# Convert the CSV data to the desired JSON format
family_tree_json = build_family_tree(csv_data)

# Print the JSON data
print(json.dumps(family_tree_json, indent=2, ensure_ascii=False))

# Optionally, write the JSON data to a file
with open('family-tree.json', 'w', encoding='utf-8') as json_file:
    json.dump(family_tree_json, json_file, ensure_ascii=False, indent=2)
