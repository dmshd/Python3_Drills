"""
This script compares two lists by hashing them and comparing the hashes.
"""

import hashlib

list1 = [1, 2, 3]
list2 = [1, 2, 3]

hash1 = hashlib.sha256(str(list1).encode()).hexdigest()
hash2 = hashlib.sha256(str(list2).encode()).hexdigest()

if hash1 == hash2:
    print("The lists contain the same data.")
else:
    print("The lists do not contain the same data.")
