#!/usr/bin/env python3
"""Extract Bing search results from saved HTML file."""
import sys, re

html = open(sys.argv[1]).read()

# Bing results are in <li class="b_algo"> blocks
results = re.findall(r'<li class="b_algo">(.*?)</li>', html, re.DOTALL)
print(f"Found {len(results)} results\n")

for i, block in enumerate(results[:12]):
    # Title
    title_m = re.search(r'<h2>.*?<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', block, re.DOTALL)
    if not title_m:
        title_m = re.search(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', block, re.DOTALL)
    
    if title_m:
        link = title_m.group(1)
        title = re.sub(r'<[^>]+>', '', title_m.group(2)).strip()
        print(f"{i+1}. {title}")
        print(f"   URL: {link}")
    
    # Snippet
    snip_m = re.search(r'<p[^>]*>(.*?)</p>', block, re.DOTALL)
    if snip_m:
        snip = re.sub(r'<[^>]+>', '', snip_m.group(1)).strip()
        if snip:
            print(f"   {snip[:200]}")
    print()