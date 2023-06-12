import heapq
import re

ip_addresses = {}


def main():
    with open("some_logs.log", "r") as file:
        lines = file.readlines()
        for line in lines:
            # Using regex to get the IP address after "SRC="
            match = re.search(r"SRC=([0-9A-Fa-f:.]+)", line)
            if match:
                ip_address = match.group(1)
                ip_addresses[ip_address] = (
                    1
                    if ip_address not in ip_addresses
                    else ip_addresses[ip_address] + 1
                )
        spammers = heapq.nlargest(3, ip_addresses, key=lambda s: ip_addresses[s])
        print("\nSpammers : ", spammers)

    for spammer in spammers:
        print(spammer, ":", ip_addresses[spammer])


if __name__ == "__main__":
    main()
