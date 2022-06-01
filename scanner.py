#! /usr/bin/env python
import req
from bs4 import BeautifulSoup


class Scanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def extract_forms(self, url=None):
        if url is None:
            url = self.target_url

        response = req.request(url)
        parsed_html = BeautifulSoup(response.content, "html.parser")
        forms_list = parsed_html.findAll("form")
        for form in forms_list:
            action = form.get("action")
            print("Action:", action)
            method = form.get("method")
            print("Method:", method)

    def extract_all_forms(self, links):
        for link in links:
            self.extract_forms(link)
