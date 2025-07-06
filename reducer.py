#!/usr/bin/python3
import sys
from collections import defaultdict

summary = defaultdict(int)
for line in sys.stdin:
    country, qty = line.strip().split("\t")
    summary[country] += int(qty)

for country, total_qty in summary.items():
    print(f"{country}\t{total_qty}")