import re

def to_filename(s: str) -> str:
    # Replace spaces with underscores
    s = s.replace(" ", "_")

    # Remove all non-alphanumeric characters
    s = re.sub(r"[^a-zA-Z0-9._-]", "", s)

    # Truncate the string to 255 characters max
    s = s[:255]

    return s
