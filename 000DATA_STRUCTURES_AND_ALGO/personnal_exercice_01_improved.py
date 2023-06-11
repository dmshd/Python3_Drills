import re


def main():
    # load the file using context manager (with statement)
    # so it will automatically close the file even if an
    # error occurs within the block.
    with open("urls.txt", "r") as file:
        # The read() method is used to read the entire
        # contents of the file into a single string.
        # Then, the splitlines() method is called on this
        # string to split the contents into a list of lines.
        lines = file.read().splitlines()
        # https://docs.python.org/3/library/stdtypes.html#str.splitlines

    # regex for removing unnecessary parts of url
    pattern = r"https?://(.*).guichet-citoyen.be"

    # loop through the lines
    slugs = [
        re.search(pattern, line).group(1) for line in lines if re.search(pattern, line)
    ]
    slugs.sort()
    print(slugs)
    print(type(slugs))

    # loop through the lines
    for slug in slugs:
        print(slug)


if __name__ == "__main__":
    main()
