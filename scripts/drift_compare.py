#!/usr/bin/env python3
"""Compare live page with its saved baseline. Usage: webdev run drift_compare.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        import hashlib
        name = hashlib.sha1(url.encode()).hexdigest()[:12]
        base = json.load(open(os.path.join('data', 'baseline-' + name + '.json')))
        status, _, html = fetch(url)
        m = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
        now = {'status': status, 'title': m.group(1).strip() if m else None,
               'h1': len(re.findall(r'<h1', html, re.I)),
               'links': len(re.findall(r'<a ', html, re.I)),
               'images': len(re.findall(r'<img', html, re.I))}
        changes = {k: {'before': base.get(k), 'now': v} for k, v in now.items() if base.get(k) != v}
        print(json.dumps({'url': url, 'changes': changes}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
