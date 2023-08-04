# url_to_html_file.py

"""
This script converts a URL to a HTML file.
"""

import sys
import urllib3

def url_to_html_file(url, html_file):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    with open(html_file, 'w') as f:
        f.write(r.data.decode('utf-8'))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python url_to_html_file.py url html_file')
        sys.exit(1)
    url = sys.argv[1]
    html_file = sys.argv[2]
    url_to_html_file(url, html_file)
