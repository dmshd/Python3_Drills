""""
Open randobel_sitemap.xml and iterate though all the URLs.
If an URl contains a query string, then it is a dynamic page.
So save each dynamic page into a file called randobel_sitemap_dynamic_pages.txt
"""

import xml.etree.ElementTree as ET

tree = ET.parse("randobel_sitemap.xml")
root = tree.getroot()

with open("randobel_sitemap_dynamic_pages.txt", "w") as f:
    for child in root:
        if "?" in child[0].text:
            f.write(child[0].text + "\n")
