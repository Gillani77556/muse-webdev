#!/usr/bin/env python3
"""Basic accessibility signals: lang, alt text, labels. Usage: webdev run accessibility_check.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        status, _, html = fetch(url)
        issues = []
        if not re.search(r'<html[^>]*lang=', html, re.I):
            issues.append('missing lang')
        if re.search(r'<img(?![^>]*alt=)', html, re.I):
            issues.append('images missing alt')
        if re.search(r'<input(?![^>]*(aria-label|id=))', html, re.I):
            issues.append('inputs may lack labels')
        print(json.dumps({'url': url, 'issues': issues, 'pass': not issues}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
