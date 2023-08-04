"""
This script shows how to save a list to a JSON file and load it back into a Python list.
"""

import json

# The list that you want to save as a JSON file
list_to_save = [1, 2, 3, 4, 5]

# Open a file in write mode
with open("list.json", "w") as outfile:
    # Write the list to the file in JSON format
    json.dump(list_to_save, outfile)

# The file is automatically closed when the with block is exited


# Open the file in read mode
with open("list.json", "r") as infile:
    # Load the JSON data from the file into a Python list
    list_from_file = json.load(infile)

# The file is automatically closed when the with block is exited

print(list_from_file)  # Output: [1, 2, 3, 4, 5]
