#! /usr/bin/env python
import req


class Crawler:
    def __init__(self, target_url, filepath):
        self.target_url = target_url
        self.filepath = filepath

    def update_url(self, target_url):
        self.target_url = target_url

    def update_filepath(self, filepath):
        self.filepath = filepath

    def crawl_subdomains(self):
        total_requests = 0
        subdomains_found = 0

        print("[*] Starting Scan...\n")
        with open(self.filepath, "r") as wordlist_file:
            for line in wordlist_file:
                word = line.strip()
                test_url = word + "." + self.target_url
                response = req.request(test_url)
                if response:
                    print("[+] Discovered subdomain -->", test_url)
                    subdomains_found += 1
                total_requests += 1

        print("\n[+] Total Requests: " + str(total_requests) + ", Discovered Subdomains: " + str(subdomains_found))
        print("[*] Scan completed.")

    def crawl_directories(self):
        total_requests = 0
        directories_found = 0

        print("[*] Starting Scan...\n")
        with open(self.filepath, "r") as wordlist_file:
            for line in wordlist_file:
                word = line.strip()
                test_url = self.target_url + "/" + word
                response = req.request(test_url)
                if response:
                    print("[+] Discovered URL -->", test_url)
                    directories_found += 1
                total_requests += 1

        print("\n[+] Total Requests: " + str(total_requests) + ", Discovered Subdomains: " + str(directories_found))
        print("[*] Scan completed.")
