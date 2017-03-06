# -*- coding: utf-8 -*-
import click
from linkedin_scraping.crawler import process
from linkedin_scraping.spider import LinkedInPeopleSpider
import sys

def main(u, p, k, f):
    # Save the username and Password in a global variable
    process.crawl(LinkedInPeopleSpider, username=u, password=p, keyword=k, filename=f)
    process.start()

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])