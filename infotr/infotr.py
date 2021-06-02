#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: infotr
Author: K4YT3X
Date Created: June 1, 2021
Last Modified: June 1, 2021
"""
from scapy.all import IP, UDP, sr1
import argparse
import contextlib
import requests
import sys


def main():
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        parser = argparse.ArgumentParser(
            prog="infotr", formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
        parser.add_argument("host", help="destination hostname")
        parser.add_argument(
            "-m", "--max", type=int, help="maximum number of hops", default=30
        )
        parser.add_argument(
            "-t", "--timeout", type=int, help="ICMP timeout in seconds", default=2
        )
        args = parser.parse_args()

        for i in range(1, args.max):
            packet = IP(dst=args.host, ttl=i) / UDP(dport=33434)

            try:
                reply = sr1(packet, verbose=0, timeout=args.timeout)
            except PermissionError:
                print("Insufficient privileges to open raw socket", file=sys.stderr)
                print(
                    "Please give Python the CAP_NET_RAW capability or run this program as root",
                    file=sys.stderr,
                )
                sys.exit(1)

            if reply is None:
                print(f"{i}: No response")
            else:
                ipinfo = requests.get(f"https://ipinfo.io/{reply.src}").json()
                print(
                    "{}: IP={},ASN={},GEO={}/{}/{}".format(
                        i,
                        reply.src,
                        ipinfo.get("org"),
                        ipinfo.get("city"),
                        ipinfo.get("region"),
                        ipinfo.get("country"),
                    )
                )

                if reply.type == 3:
                    print("Trace Completed")
                    break
        else:
            print(f"Maximum ({args.max}) hops reached")
