#!/usr/bin/env python3
"""Search duckduckgo and print results."""
import sys, re, urllib.request, urllib.parse

query = sys.argv[1] if len(sys.argv) > 1 else "test"
url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="replace")

results = re.findall(r'<a[^>]*class="result__a"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>', html)
snippets = re.findall(r'<a[^>]*class="result__snippet"[^>]*>([^<]+)</a>', html)

for i, (link, title) in enumerate(results[:12]):
    snippet = snippets[i] if i < len(snippets) else ""
    clean_title = re.sub(r'<[^>]+>', '', title).strip()
    print(f"{i+1}. {clean_title}")
    print(f"   URL: {link}")
    if snippet:
        clean_snippet = re.sub(r'<[^>]+>', '', snippet).strip()
        print(f"   {clean_snippet}")
    print()