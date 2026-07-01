#!/usr/bin/env python3
"""Extract Bing b_algo results from saved HTML file."""
import sys, re

html = open(sys.argv[1]).read()

# Find b_algo blocks
pattern = r'<li[^>]*class="b_algo"[^>]*>(.*?)</li>'
blocks = re.findall(pattern, html, re.DOTALL)
print(f"Found {len(blocks)} b_algo blocks", file=sys.stderr)

for i, block in enumerate(blocks[:12]):
    # Find <h2><a href="..." ...>Title</a></h2>
    m = re.search(r'<h2>(.*?)</h2>', block, re.DOTALL)
    if m:
        h2 = m.group(1)
        link_m = re.search(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', h2, re.DOTALL)
        if link_m:
            url = link_m.group(1)
            title = re.sub(r'<[^>]+>', '', link_m.group(2)).strip()
            print(f"{i+1}. {title}")
            print(f"   {url}")
    
    # Find snippet <p>
    p_m = re.search(r'<p[^>]*>(.*?)</p>', block, re.DOTALL)
    if p_m:
        p_text = re.sub(r'<[^>]+>', '', p_m.group(1)).strip()
        if p_text:
            print(f"   {p_text[:200]}")
    print()

# If no b_algo found, dump a summary of classes found
if len(blocks) == 0:
    classes = re.findall(r'class="([^"]*b_algo[^"]*)"', html)
    print(f"Classes with b_algo: {classes}", file=sys.stderr)
    # Also try to find any li elements
    lis = re.findall(r'<li[^>]*>', html)
    print(f"Total li tags: {len(lis)}", file=sys.stderr)
    for li in lis[:20]:
        print(f"  {li[:150]}", file=sys.stderr)