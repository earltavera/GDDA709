#!/usr/bin/python3
import sys

for line in sys.stdin:
    fields = line.strip().split(",")
    if fields[1] != "Country" and len(fields) == 8:
        try:
            country = fields[1].strip()
            temperature = int(fields[7])
            print(f"{country}\t{temperature}")
        except ValueError:
            continue