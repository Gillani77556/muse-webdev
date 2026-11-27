#!/usr/bin/env python3
"""Save a baseline snapshot to data/. Usage: webdev run drift_baseline.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        import hashlib
        status, _, html = fetch(url)
        m = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
        snap = {'url': url, 'status': status,
                'title': m.group(1).strip() if m else None,
                'h1': len(re.findall(r'<h1', html, re.I)),
                'links': len(re.findall(r'<a ', html, re.I)),
                'images': len(re.findall(r'<img', html, re.I))}
        name = hashlib.sha1(url.encode()).hexdigest()[:12]
        os.makedirs('data', exist_ok=True)
        path = os.path.join('data', 'baseline-' + name + '.json')
        open(path, 'w').write(json.dumps(snap, indent=2))
        print(json.dumps({'saved': path, **snap}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
