"""Shared helpers for muse-webdev scripts: safe URL validation + fetch."""
import re, sys, urllib.request, urllib.error
from urllib.parse import urlparse

def validate_url(url):
    p = urlparse(url)
    if p.scheme not in ("http", "https") or not p.hostname:
        raise ValueError("URL must be http(s) with a hostname")
    # Block private / loopback hosts (SSRF guard, same idea as claude-seo)
    host = p.hostname.lower()
    if host in ("localhost",) or host.endswith(".local") or host.startswith("10.") \
       or host.startswith("192.168.") or host.startswith("172.16."):
        raise ValueError("refused: non-public host")
    return url

def fetch(url, timeout=20):
    validate_url(url)
    req = urllib.request.Request(url, headers={"User-Agent": "muse-webdev/0.2.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.headers, r.read().decode("utf-8", errors="ignore")

def main_arg():
    if len(sys.argv) < 2:
        print("usage: <script.py> <url>", file=sys.stderr); sys.exit(2)
    return sys.argv[1]
