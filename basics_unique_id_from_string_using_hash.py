"""
Generate a unique ID for the element using the sha256() function
"""

import hashlib

name = "VTT du Grand Raid Godefroid 70 km"

# Generate a unique ID for the element using the sha256() function
unique_id = hashlib.sha256(name.encode()).hexdigest()

print(unique_id)
