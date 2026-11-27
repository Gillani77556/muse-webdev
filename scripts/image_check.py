#!/usr/bin/env python3
"""Images on a page: count and missing alt text. Usage: webdev run image_check.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        status, _, html = fetch(url)
        imgs = re.findall(r'<img[^>]*>', html, re.I)
        missing = [i for i in imgs if 'alt=' not in i.lower()]
        print(json.dumps({'url': url, 'images': len(imgs), 'missing_alt': len(missing)}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
