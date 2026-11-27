#!/usr/bin/env python3
"""Measure response time and page weight. Usage: webdev run performance_check.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        import time
        t0 = time.time()
        status, _, html = fetch(url)
        secs = round(time.time() - t0, 2)
        print(json.dumps({'url': url, 'status': status, 'ttfb_seconds': secs,
                          'bytes': len(html), 'heavy': len(html) > 500000}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
