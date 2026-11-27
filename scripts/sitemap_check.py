#!/usr/bin/env python3
"""Fetch /sitemap.xml and report URL count. Usage: webdev run sitemap_check.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        base = url.rstrip('/')
        try:
            s, _, xml = fetch(base + '/sitemap.xml')
            out = {'sitemap': base + '/sitemap.xml', 'status': s,
                   'urls': len(re.findall(r'<loc>', xml))}
        except Exception as e:
            out = {'sitemap': base + '/sitemap.xml', 'status': None, 'error': str(e)}
        print(json.dumps(out))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
