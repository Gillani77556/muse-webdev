#!/usr/bin/env python3
"""Parse HTML: headings, links, images, forms count. Usage: webdev run parse_html.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        status, _, html = fetch(url)
        print(json.dumps({'url': url, 'status': status,
                          'h1': len(re.findall(r'<h1', html, re.I)),
                          'h2': len(re.findall(r'<h2', html, re.I)),
                          'links': len(re.findall(r'<a ', html, re.I)),
                          'images': len(re.findall(r'<img', html, re.I)),
                          'forms': len(re.findall(r'<form', html, re.I)),
                          'images_missing_alt': len(re.findall(r'<img(?![^>]*alt=)', html, re.I))}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
