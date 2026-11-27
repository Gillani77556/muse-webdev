#!/usr/bin/env python3
"""Mechanical page checks: title, H1, meta description. Usage: webdev run page_checks.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        status, _, html = fetch(url)
        issues = []
        if not re.search(r'<title>[^<]+</title>', html, re.I):
            issues.append('missing title')
        if len(re.findall(r'<h1', html, re.I)) != 1:
            issues.append('h1 count is not 1')
        if not re.search(r'name="description"', html, re.I):
            issues.append('missing meta description')
        print(json.dumps({'url': url, 'status': status, 'issues': issues, 'pass': not issues}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
