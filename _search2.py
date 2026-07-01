#!/usr/bin/env python3
"""Search using alternative approach - save to temp file first."""
import sys, re, urllib.request, urllib.parse, os

query = sys.argv[1] if len(sys.argv) > 1 else "digital marketing agency"
url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
})
try:
    resp = urllib.request.urlopen(req, timeout=20)
    html = resp.read().decode("utf-8", errors="replace")
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)

# Try different patterns
for pattern_name, pattern in [
    ("result__a", r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>'),
    ("result-url", r'class="result__url"[^>]*href="([^"]+)"'),
    ("result-title", r'class="result__title"[^>]*>.*?<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>'),
    ("A tag", r'<a[^>]*rel="nofollow"[^>]*href="([^"]+)"[^>]*>(.*?)</a>'),
    ("article", r'<article[^>]*>.*?<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>'),
]:
    matches = re.findall(pattern, html, re.DOTALL)
    if matches:
        print(f"\n--- Pattern: {pattern_name} -> {len(matches)} matches ---")
        for i, m in enumerate(matches[:8]):
            link = m[0] if isinstance(m, tuple) else m
            title = re.sub(r'<[^>]+>', '', m[1] if isinstance(m, tuple) else '').strip()
            print(f"{i+1}. {title[:80]}")
            print(f"   {link[:120]}")

# Also dump a portion of HTML to see structure
print("\n--- HTML snippet ---")
# Find search results area
idx = html.find('class="results"')
if idx < 0:
    idx = html.find('id="links"')
if idx < 0:
    idx = html.find('class="web-result"')
if idx < 0:
    idx = 5000
print(html[max(0,idx-200):idx+1500])