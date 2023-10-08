import os
import json

# Get the current working directory
json_directory = os.getcwd()

# Initialize a dictionary to store JSON content with relationships
json_data = {}

# Function to recursively build the family tree
def build_family_tree(person_id):
    person = json_data[person_id]
    children = []
    for potential_child_id, potential_child in json_data.items():
        if (
            "parent_id" in potential_child
            and potential_child["parent_id"] == person_id
        ):
            # Check if the child has a parent_id, and if not, set it to the ID of the parent
            if "parent_id" not in potential_child:
                potential_child["parent_id"] = person_id
            children.extend(build_family_tree(potential_child_id))
            person["children"] = children
    return [person]

# Iterate through files in the directory
for filename in os.listdir(json_directory):
    if filename.endswith(".json"):
        # Read and parse the JSON file
        print(filename)
        with open(os.path.join(json_directory, filename), 'r') as json_file:
            json_content = json.load(json_file)
        
        # Use "name" as the identifier if "id" is not present
        person_id = json_content.get("id", json_content.get("name"))

        # Add the JSON content to the dictionary with the person's identifier as the key
        json_data[person_id] = json_content

# Find the person with a parent_id of "*"
root_person = None
for person_id, person in json_data.items():
    if "parent_id" in person and person["parent_id"] == "*":
        root_person = person_id
        break

# Build the family tree starting from the person with parent_id "*"
family_tree = build_family_tree(root_person)

# Convert the family tree (root person and descendants) to a JSON string
family_tree_json_string = json.dumps(family_tree, indent=2)

# Write the family tree JSON string to a Markdown file
with open('familytree.md', 'w') as md_file:
    md_file.write(family_tree_json_string)
