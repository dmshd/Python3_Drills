"""
Scrap favicon asset from a website.
"""

import os
import sys
import urllib.request
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

def scrap_favicon(url):
    """
    Scrap favicon from a website.
    """
    # Get the domain name
    domain_name = urlparse(url).netloc
    # Get the favicon url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    favicon_url = soup.find('link', rel='shortcut icon')['href']
    # Download the favicon
    urllib.request.urlretrieve(favicon_url, 'favicon' + '.ico')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 scrap_favicon.py <url>')
        sys.exit(1)
    url = sys.argv[1]
    scrap_favicon(url)
