#!/usr/bin/env python3
"""Check security headers. Usage: webdev run security_headers.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        status, headers, _ = fetch(url)
        keys = [k.lower() for k in headers.keys()]
        wanted = ['strict-transport-security', 'content-security-policy',
                  'x-frame-options', 'x-content-type-options']
        print(json.dumps({'url': url, 'status': status,
                          'present': [h for h in wanted if h in keys],
                          'missing': [h for h in wanted if h not in keys]}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
