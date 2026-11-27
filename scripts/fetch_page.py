#!/usr/bin/env python3
"""Fetch a page and report status, size and title. Usage: webdev run fetch_page.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        status, _, html = fetch(url)
        m = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
        print(json.dumps({'url': url, 'status': status, 'bytes': len(html),
                          'title': m.group(1).strip() if m else None}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
