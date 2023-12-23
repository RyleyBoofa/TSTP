import urllib.request

from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        # create a list to store headlines
        headlines = []
        
        # make a request to site and return a response object containing HTML
        r = urllib.request.urlopen(self.site)
        # return the HTML from the response object
        html = r.read()

        # create a BeautifulSoup object, passing it the html and parse parameters
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)

        # find_all method returns iterable containing all found <a> tags
        for tag in sp.find_all("a"):
            # get the href attribute from the <a> tag
            url = tag.get("href")
            # ensure URL links is valid
            if url is None:
                continue
            # print the found URL's
            if "http" in url:
                headlines.append(url)

        # write the headline URL's to a file
        with open("headlines.txt", "w") as f:
            for hl in headlines:
                f.write(hl)
                f.write("\n")

news = "https://news.google.com/"
Scraper(news).scrape()
