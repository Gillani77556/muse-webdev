#!/usr/bin/env python3
"""Find JSON-LD blocks and list their @type values. Usage: webdev run schema_check.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        status, _, html = fetch(url)
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.I | re.S)
        types = []
        for b in blocks:
            try:
                types.append(json.loads(b).get('@type'))
            except Exception:
                types.append(None)
        print(json.dumps({'url': url, 'json_ld_blocks': len(blocks), 'types': types}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
