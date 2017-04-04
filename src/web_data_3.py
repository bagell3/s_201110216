import lxml.html
from lxml.cssselect import CSSSelector
import requests

url = requests.get('http://www.google.com/search?q=python')
tree = lxml.html.fromstring(url.text)
link = CSSSelector('a[href]')
lines = link(tree)
print len(save)

for line in lines:
    save = lxml.html.tostring(line)
    if 'https://' in save:
        print save 
        print 