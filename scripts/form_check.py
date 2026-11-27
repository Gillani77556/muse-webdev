#!/usr/bin/env python3
"""Forms on a page: count, method, inputs. Usage: webdev run form_check.py <url>"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from url_safety import fetch, main_arg

if __name__ == "__main__":
    url = main_arg()
    try:
        status, _, html = fetch(url)
        forms = re.findall(r'<form[^>]*>', html, re.I)
        print(json.dumps({'url': url, 'forms': len(forms),
                          'inputs': len(re.findall(r'<input', html, re.I)),
                          'textareas': len(re.findall(r'<textarea', html, re.I))}))
    except Exception as e:
        print(json.dumps({"url": url, "error": str(e)}))
        sys.exit(1)
