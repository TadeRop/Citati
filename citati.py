from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'http://quotes.yourdictionary.com/theme/marriage/'
response = urlopen(url).read()
soup = BeautifulSoup(response)

for quote in soup.findAll("p"):
    quotes = soup.find("p", attrs={"class": "quoteContent"}).string
    print quotes


