#!/usr/bin/env python3
"""List links on a page and check each returns 200. Usage: webdev run broken_links.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        status, _, html = fetch(url)
        links = sorted(set(re.findall(r'href="(https?://[^"]+)"', html)))
        results = []
        for link in links[:30]:
            try:
                s, _, _ = fetch(link)
                results.append({'link': link, 'status': s})
            except Exception as e:
                results.append({'link': link, 'status': None, 'error': str(e)})
        broken = [r for r in results if r.get('status') != 200]
        print(json.dumps({'url': url, 'checked': len(results), 'broken': broken}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
