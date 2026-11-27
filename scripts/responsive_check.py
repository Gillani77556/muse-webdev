#!/usr/bin/env python3
"""Viewport meta and fixed-width overflow risks. Usage: webdev run responsive_check.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        status, _, html = fetch(url)
        print(json.dumps({'url': url,
                          'viewport_meta': bool(re.search(r'name=["\']?viewport', html, re.I)),
                          'fixed_width_px': len(re.findall(r'width:\s*\d{3,4}px', html)),
                          'tables': len(re.findall(r'<table', html, re.I))}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
