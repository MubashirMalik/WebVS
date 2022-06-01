#! /usr/bin/env python
import requests
import urllib3


def request(url):
    if "http" not in url:
        url = "http://" + url

    try:
        return requests.get(url)
    except requests.exceptions.InvalidURL:
        print("[-] URL is invalid -->", url)
    except requests.exceptions.MissingSchema:
        print("[-] URL is invalid -->", url)
    except urllib3.exceptions.LocationParseError:
        print("[-] URL is invalid -->", url)
    except requests.exceptions.ConnectionError:
        pass
