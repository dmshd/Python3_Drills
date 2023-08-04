"""
This script compares two lists by converting them to JSON and comparing the JSON.
"""

import json

list1 = [1, 2, 3]
list2 = [1, 2, 3]

json1 = json.dumps(list1)
json2 = json.dumps(list2)

if json1 == json2:
    print("The lists contain the same data.")
else:
    print("The lists do not contain the same data.")
