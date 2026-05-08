
import requests
from bs4 import BeautifulSoup
from typing import List, Dict

class BusinessTrendCrawler:
    def __init__(self):
        self.sources = [
            "https://news.google.com/rss/search?q=business+trends+global+top+1%25&hl=en-US&gl=US&ceid=US:en"
        ]

    def crawl(self) -> List[Dict[str, str]]:
        trends = []
        for url in self.sources:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'xml')
                items = soup.find_all('item')
                for item in items:
                    trends.append({
                        "title": item.title.text,
                        "link": item.link.text,
                        "pubDate": item.pubDate.text,
                        "description": item.description.text
                    })
            except Exception as e:
                print(f"Error crawling {url}: {e}")
        return trends

if __name__ == "__main__":
    crawler = BusinessTrendCrawler()
    results = crawler.crawl()
    for res in results[:5]:
        print(f"Trend: {res['title']}")
