#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re

# country = open('afghanistan.html', 'r').read()
country = open('test.html', 'r').read()

def parse_country(html):
    soup = BeautifulSoup(html)

    # h2s = ['Introduction', 'At a Glance', 'Key Indicators',
    #       'International Rankings', 'Legal Snapshot', 'Legal Analysis',
    #       'Reports', 'News and Additional Resources']

    h2s = ['Introduction', 'Another heading', 'Heading 3']

    scraped_data = {}

    tags_in_h2 = soup.select('#content h2 *')
    [tag.extract() for tag in tags_in_h2]

    for h2 in h2s:
        headings = soup.find(id='content').find("h2", text=h2)

        content = []

        if headings is not None:
            next_tag = headings.next_sibling
            while next_tag is not None and next_tag.name != 'h2':
                if next_tag != '\n':
                    content.append(next_tag)
                next_tag = next_tag.next_sibling

        scraped_data[h2] = content

    return(scraped_data)

print(parse_country(country))
