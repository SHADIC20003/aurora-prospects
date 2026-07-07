#!/usr/bin/env python3
import json

with open("/home/gaster/Documents/github/aurora-prospects/seen-agencies.json") as f:
    data = json.load(f)

names = [a["name"].lower() for a in data["agencies"]]
print(f"Total seen: {len(names)}")
print(f"Version: {data['version']}")