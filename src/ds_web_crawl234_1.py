from bs4 import BeautifulSoup
import urllib

html = urllib.urlopen("https://www.python.org/")
soup = BeautifulSoup(html,'lxml')
_href = soup.findAll('a')
n=0
for line in _href:
    if 'http://' in line['href']:
        if n<50:
            print n, line['href']
        n+=1
print "total: ", n