"""
This was made as an exercise to find the top 3 IP addresses that are spamming my server.

some_logs.log is a file that contains logs from my server. I have removed the IP of my server for privacy reasons.

Here is a sample :

Jun 11 17:18:10 vps-0e3c54e3 kernel: [27761.311719] [UFW BLOCK] IN=ens3 OUT= MAC=[MAC_ADDRESS] SRC=94.102.61.5 DST=[DST_IP] LEN=44 TOS=0x00 PREC=0x00 TTL=242 ID=54321 PROTO=TCP SPT=48542 DPT=12186 WINDOW=65535 RES=0x00 SYN URGP=0
Jun 11 17:18:24 vps-0e3c54e3 kernel: [27774.947452] [UFW BLOCK] IN=ens3 OUT= MAC=[MAC_ADDRESS] SRC=95.214.53.99 DST=[DST_IP] LEN=40 TOS=0x00 PREC=0x00 TTL=241 ID=54321 PROTO=TCP SPT=58659 DPT=5593 WINDOW=65535 RES=0x00 SYN URGP=0
Jun 11 17:18:39 vps-0e3c54e3 kernel: [27789.818812] [UFW BLOCK] IN=ens3 OUT= MAC=[MAC_ADDRESS] SRC=62.233.50.217 DST=[DST_IP] LEN=40 TOS=0x00 PREC=0x00 TTL=241 ID=4952 PROTO=TCP SPT=52203 DPT=65401 WINDOW=1024 RES=0x00 SYN URGP=0
Jun 11 17:19:04 vps-0e3c54e3 kernel: [27814.856008] [UFW BLOCK] IN=ens3 OUT= MAC=[MAC_ADDRESS] SRC=59.49.193.83 DST=[DST_IP] LEN=540 TOS=0x00 PREC=0x00 TTL=37 ID=34811 PROTO=UDP SPT=45613 DPT=46433 LEN=520
Jun 11 17:19:30 vps-0e3c54e3 kernel: [27840.573436] [UFW BLOCK] IN=ens3 OUT= MAC=[MAC_ADDRESS] SRC=162.142.125.130 DST=[DST_IP] LEN=44 TOS=0x00 PREC=0x00 TTL=32 ID=45602 PROTO=TCP SPT=23783 DPT=17777 WINDOW=1024 RES=0x00 SYN URGP=0
Jun 11 17:19:41 vps-0e3c54e3 kernel: [27852.057174] [UFW BLOCK] IN=ens3 OUT= MAC=[MAC_ADDRESS] SRC=94.102.61.40 DST=[DST_IP] LEN=40 TOS=0x00 PREC=0x00 TTL=242 ID=54321 PROTO=TCP SPT=50393 DPT=49200 WINDOW=65535 RES=0x00 SYN URGP=0
Jun 11 17:20:01 vps-0e3c54e3 CRON[22880]: (smmsp) CMD (test -x /etc/init.d/sendmail && test -x /usr/share/sendmail/sendmail && test -x /usr/libexec/sendmail/sendmail && /usr/share/sendmail/sendmail cron-msp)
Jun 11 17:20:29 vps-0e3c54e3 kernel: [27900.145340] [UFW BLOCK] IN=ens3 OUT= MAC=[MAC_ADDRESS] SRC=168.232.13.171 DST=[DST_IP] LEN=44 TOS=0x00 PREC=0x00 TTL=233 ID=30151 DF PROTO=TCP SPT=4864 DPT=23 WINDOW=14600 RES=0x00 SYN URGP=0
...

"""

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

# Output:
"""
Spammers :  ['141.105.67.7', '89.248.162.159', '95.214.53.99']
141.105.67.7 : 40
89.248.162.159 : 34
95.214.53.99 : 15
"""
