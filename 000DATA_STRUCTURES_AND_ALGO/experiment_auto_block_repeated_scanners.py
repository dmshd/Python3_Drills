"""
This was made as an experiment to find the reccurent IP addresses that were
scanning my server.

The script reads the /var/log/syslog file and finds the IP addresses that are
trying to connect to the server the most.
It then blocks the IP addresses using the ufw command.

Example of the /var/log/syslog file:

Jun 11 17:18:10 vps-0e3c54e3 kernel: [27761.311719] [UFW BLOCK] IN=ens3 OUT=
MAC=[MAC_ADDRESS] SRC=94.102.61.5 DST=[DST_IP] LEN=44 TOS=0x00 PREC=0x00
TTL=242 ID=54321 PROTO=TCP SPT=48542 DPT=12186 WINDOW=65535 RES=0x00 SYN URGP=0

Jun 11 17:18:24 vps-0e3c54e3 kernel: [27774.947452] [UFW BLOCK] IN=ens3 OUT=
MAC=[MAC_ADDRESS] SRC=95.214.53.99 DST=[DST_IP] LEN=40 TOS=0x00 PREC=0x00
TTL=241 ID=54321 PROTO=TCP SPT=58659 DPT=5593 WINDOW=65535 RES=0x00 SYN URGP=0

Jun 11 17:18:39 vps-0e3c54e3 kernel: [27789.818812] [UFW BLOCK] IN=ens3 OUT=
MAC=[MAC_ADDRESS] SRC=62.233.50.217 DST=[DST_IP] LEN=40 TOS=0x00 PREC=0x00
TTL=241 ID=4952 PROTO=TCP SPT=52203 DPT=65401 WINDOW=1024 RES=0x00 SYN URGP=0

Jun 11 17:19:04 vps-0e3c54e3 kernel: [27814.856008] [UFW BLOCK] IN=ens3 OUT=
MAC=[MAC_ADDRESS] SRC=59.49.193.83 DST=[DST_IP] LEN=540 TOS=0x00 PREC=0x00
TTL=37 ID=34811 PROTO=UDP SPT=45613 DPT=46433 LEN=520

Jun 11 17:19:30 vps-0e3c54e3 kernel: [27840.573436] [UFW BLOCK] IN=ens3 OUT=
MAC=[MAC_ADDRESS] SRC=162.142.125.130 DST=[DST_IP] LEN=44 TOS=0x00 PREC=0x00
TTL=32 ID=45602 PROTO=TCP SPT=23783 DPT=17777 WINDOW=1024 RES=0x00 SYN URGP=0

Jun 11 17:19:41 vps-0e3c54e3 kernel: [27852.057174] [UFW BLOCK] IN=ens3 OUT=
MAC=[MAC_ADDRESS] SRC=94.102.61.40 DST=[DST_IP] LEN=40 TOS=0x00 PREC=0x00
TTL=242 ID=54321 PROTO=TCP SPT=50393 DPT=49200 WINDOW=65535 RES=0x00 SYN URGP=0

Jun 11 17:20:29 vps-0e3c54e3 kernel: [27900.145340] [UFW BLOCK] IN=ens3 OUT=
MAC=[MAC_ADDRESS] SRC=168.232.13.171 DST=[DST_IP] LEN=44 TOS=0x00 PREC=0x00
TTL=233 ID=30151 DF PROTO=TCP SPT=4864 DPT=23 WINDOW=14600 RES=0x00 SYN URGP=0

blocked_ips.txt sample :
124.156.238.47
43.130.10.173
103.178.229.195
108.167.178.116
2a06:4880:a000:0000:0000:0000:0000:00d6
69.50.94.76
168.121.27.66

ip_blocked.log sample :
2023-06-12 19:09:10,596 INFO Blocked IP address 43.130.10.173
2023-06-12 19:09:10,798 INFO Blocked IP address 103.178.229.195
2023-06-12 19:09:11,037 INFO Blocked IP address 108.167.178.116
2023-06-12 19:09:11,242 INFO Blocked IP address
2a06:4880:a000:0000:0000:0000:0000:00d6
2023-06-12 19:09:11,491 INFO Blocked IP address 69.50.94.76
2023-06-12 19:09:11,671 INFO Blocked IP address 168.121.27.66
"""

import heapq
import logging
import os
import re
import subprocess
from logging.handlers import TimedRotatingFileHandler

# Configure logging
LOG_FILENAME = "ip_blocked.log"
logger = logging.getLogger("")  # Get the root logger
logger.setLevel(logging.INFO)  # Set the logger's level
# Create a TimedRotatingFileHandler for the logger
logHandler = TimedRotatingFileHandler(LOG_FILENAME, when="midnight", interval=1)
logFormatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
logHandler.setFormatter(logFormatter)
logger.handlers = []
logger.addHandler(logHandler)


ip_addresses = {}
BLOCKED_IP_ADDRESSES_FILEPATH = "blocked_ips.txt"


def main():
    blocked_ips = load_blocked_ips()

    with open("/var/log/syslog", "r") as file:
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
        spammers = heapq.nlargest(259, ip_addresses, key=lambda s: ip_addresses[s])
        print("\nSpammers : ", spammers)

    for spammer in spammers:
        if spammer not in blocked_ips:
            print("SPAMMER : ", spammer)
            block_ip(spammer)
            blocked_ips.append(spammer)
            save_blocked_ips(blocked_ips)


def load_blocked_ips():
    """
    Load blocked IP addresses from the blocked_ips.txt file.
    """
    if os.path.exists(BLOCKED_IP_ADDRESSES_FILEPATH):
        with open(BLOCKED_IP_ADDRESSES_FILEPATH, "r") as file:
            blocked_ips = file.read().splitlines()
            # print("Blocked IPs (file):\n", blocked_ips)
            # Output:
            # Blocked IPs (file):
            # ['45.134.144.212', '95.214.53.99', '89.248.162.159',
            # '141.105.67.7', '51.15.34.47', '89.248.163.19',
            # '51.158.167.216', ...]
            return blocked_ips
    else:
        blocked_ips = set()
    return blocked_ips


def save_blocked_ips(blocked_ips):
    """
    Save blocked IP addresses to the blocked_ips.txt file.
    """
    with open(BLOCKED_IP_ADDRESSES_FILEPATH, "w") as file:
        for ip in blocked_ips:
            file.write(ip + "\n")


def block_ip(ip_address):
    """
    Block a given IP address using ufw and log the action
    """
    try:
        subprocess.run(["sudo", "ufw", "deny", "from", f"{ip_address}", "to", "any"])
        logging.info(f"Blocked IP address {ip_address}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to block IP address {ip_address} : {e}")


if __name__ == "__main__":
    main()
