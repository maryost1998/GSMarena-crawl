from Specifications import Specifications
from crawler import CrawlerLinks, DataCrawler

import sys

from pictures import Pictures

if __name__ == "__main__":

    switch = sys.argv[1]
    if switch == 'find_links':
        crawler = CrawlerLinks()
        crawler.start(store=False)

    if switch == 'get_data':
        crawler = DataCrawler()
        crawler.start(store=True)

    # pictures = Pictures()
    # pictures.get_link()
    # pictures.get_picture()
