# impavide_scrap_nouveautes.py

"""
Scraps ul elements that follows a h4 element with the text Nouveautés.
"""

import os
import sys
import urllib.request
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def look_through(element):
    """
    Print the type, attributes and the methods of a Python element.
    """
    print('Type: {}'.format(type(element)))
    print('Attributes:')
    print(dir(element))
    print('Methods:')
    print([method for method in dir(element) if callable(getattr(element, method))])


def scrap_nouveautes(url):
    """
    Scrap ul elements that follows a h4 element with the text Nouveautés.
    """
    # Get the domain name
    domain_name = urlparse(url).netloc
    # Get the favicon url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    nouveautes_titre = soup.findAll('h4', text='Corrections')
    print(look_through(nouveautes_titre))
    with open('corr.md', 'w') as f:
        for el in nouveautes_titre:
            nouveautes = el.findNext('ul').findAll('li')
            for nouveaute in nouveautes:
                print(f'* {nouveaute.text.strip()}', file=f)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 scrap_nouveautes.py <url>')
        sys.exit(1)
    url = sys.argv[1]
    scrap_nouveautes(url)