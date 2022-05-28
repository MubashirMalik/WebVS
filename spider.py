#! /usr/bin/env python
import req
import re
from urllib.parse import urljoin


def extract_links_from(url):
    response = req.request(url)
    return re.findall('(?:href=")(.*?)"', str(response.content))


class Spider:
    def __init__(self, target_url):
        self.target_url = target_url
        self.target_links = []

    def crawl(self, target_url):
        href_links = extract_links_from(target_url)

        for link in href_links:
            link = urljoin(target_url, link)

            if "#" in link:
                link = link.split("#")[0]

            if target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)
