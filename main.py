#! /usr/bin/env python
import crawler
import spider
import scanner


if __name__ == "__main__":

    print("Web Information Gathering")
    print("-------------------------")
    print("[1] Crawl Subdomains")
    print("[2] Crawl Directories/Files/Folders")
    print("[3] Extract Links from Website")
    print("[4] Extract Forms")
    print()

    choice = int(input("Enter your choice: "))
    print()

    if choice == 1:
        target_url = input("Enter target URL (e.g., google.com): ")
        filepath = input("Enter filepath of wordlist: ")
        print()

        crawler = crawler.Crawler(target_url, filepath)
        crawler.crawl_subdomains()
    elif choice == 2:
        target_url = input("Enter target URL (e.g., www.google.com): ")
        filepath = input("Enter filepath of wordlist: ")
        print()

        crawler = crawler.Crawler(target_url, filepath)
        crawler.crawl_directories()
    elif choice == 3:
        target_url = input("Enter target URL (e.g., daraz.com): ")
        print()

        spider = spider.Spider(target_url)
        print("[*] Starting Spider...\n")
        spider.crawl(target_url)
        print("\n[*] Crawl completed.")
    elif choice == 4:
        target_url = input("Enter target URL (e.g., https://flexstudent.nu.edu.pk/Login): ")
        print()

        scanner = scanner.Scanner(target_url)
        print("[*] Starting Scanner...\n")
        scanner.extract_forms()
        print("\n[*] Scan completed.")
