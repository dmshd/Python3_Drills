import re

ip_addresses = {}


def main():
    with open("some_logs.log", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            # Using regex to get the IP address after "SRC="
            match = re.search(r"SRC=([0-9A-Fa-f:.]+)", line)
            if match:
                ip_address = match.group(1)
                print(ip_address)
                print(type(ip_address))
                ip_addresses[ip_address] = ip_addresses.get(ip_address, 0) + 1

    print(ip_addresses)


if __name__ == "__main__":
    main()
