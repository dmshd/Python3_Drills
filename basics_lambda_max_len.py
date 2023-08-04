"""
This script shows how to use lambda function with max() function to find the
longest element in a list of strings.
"""

biggest_element = max(element, key=lambda x: len(x.text))
