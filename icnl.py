#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re

# country = open('afghanistan.html', 'r').read()
# country = open('test.html', 'r').read()

class Report:
    """docstring for Report"""
    def __init__(self, html_file):
        super(Report, self).__init__()
        self.parse_country(html_file)

    def parse_country(self, html_file):
        soup = BeautifulSoup(open(html_file, 'r'))

        # h2s = ['Introduction', 'At a Glance', 'Key Indicators',
        #       'International Rankings', 'Legal Snapshot', 'Legal Analysis',
        #       'Reports', 'News and Additional Resources']

        h2s = [('introduction', 'Introduction'), ('glance', 'At a Glance'),
               ('legal', 'Legal Snapshot')]

        tags_in_h2 = soup.select('#content h2 *')
        [tag.extract() for tag in tags_in_h2]

        for h2_name, h2 in h2s:
            headings = soup.find(id='content').find("h2", text=h2)

            content = []

            if headings is not None:
                next_tag = headings.next_sibling
                while next_tag is not None and next_tag.name != 'h2':
                    if next_tag != '\n':
                        content.append(next_tag)
                    next_tag = next_tag.next_sibling

            content_html = '\n'.join([str(tag) for tag in content])
            content_plain = '\n'.join([tag.text for tag in content])
            setattr(self, h2_name, content_html)
            setattr(self, h2_name + '_plain', content_plain)

asdf = Report('afghanistan.html')
print(asdf.introduction_plain)
