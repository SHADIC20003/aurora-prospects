#!/usr/bin/env python3
"""Update seen-agencies.json with new agencies."""
import json

with open('/home/gaster/Documents/github/aurora-prospects/seen-agencies.json') as f:
    data = json.load(f)

new_agencies = [
    {"name": "Acceleration Partners", "source_date": "2026-07-01", "source_url": "archive/2026-07-01.html"},
    {"name": "Canny", "source_date": "2026-07-01", "source_url": "archive/2026-07-01.html"},
    {"name": "Coda", "source_date": "2026-07-01", "source_url": "archive/2026-07-01.html"},
    {"name": "Grant Thornton", "source_date": "2026-07-01", "source_url": "archive/2026-07-01.html"},
    {"name": "Happy Cog", "source_date": "2026-07-01", "source_url": "archive/2026-07-01.html"},
    {"name": "JKR (Jones Knowles Ritchie)", "source_date": "2026-07-01", "source_url": "archive/2026-07-01.html"},
    {"name": "KPMG", "source_date": "2026-07-01", "source_url": "archive/2026-07-01.html"},
    {"name": "Logical Position", "source_date": "2026-07-01", "source_url": "archive/2026-07-01.html"},
    {"name": "Red Antler", "source_date": "2026-07-01", "source_url": "archive/2026-07-01.html"},
    {"name": "Typeform", "source_date": "2026-07-01", "source_url": "archive/2026-07-01.html"},
    {"name": "Ustwo", "source_date": "2026-07-01", "source_url": "archive/2026-07-01.html"},
]

# Check for duplicates
existing_names = {a['name'].lower() for a in data['agencies']}
for a in new_agencies:
    if a['name'].lower() in existing_names:
        print(f"WARNING: {a['name']} already exists!")
    else:
        data['agencies'].append(a)

# Sort alphabetically
data['agencies'].sort(key=lambda x: x['name'].lower())

# Update version and date
data['version'] = data['version'] + 1
data['last_updated'] = '2026-07-01'

with open('/home/gaster/Documents/github/aurora-prospects/seen-agencies.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Updated: version {data['version']}, {len(data['agencies'])} total agencies")
print(f"Added: {len(new_agencies)} new agencies")