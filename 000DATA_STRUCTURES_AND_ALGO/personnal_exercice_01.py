def main():
    # load the file
    file = open("urls.txt", "r")
    # breakpoint()
    # read the file
    lines = file.readlines()

    slugs = []

    # loop through the lines
    for line in lines:
        # clean the line
        line = line.strip()
        line = line.replace("https://", "")
        line = line.replace(".be", "")
        line = line.replace("www.", "")
        line = line.replace(".guichet-citoyen", "")
        if line.endswith("imio"):
            line = line.replace("my.", "")
        if line.startswith("e-guichet."):
            line = line.replace("e-guichet.", "")
        slugs.append(line)

    slugs.sort()

    # loop through the lines
    for slug in slugs:
        print(slug)

    # close the file
    file.close()


if __name__ == "__main__":
    main()
