# coding: utf-8
import lxml.html
from lxml.cssselect import CSSSelector
import requests
link=requests.get('http://www.ieee.org/conferences_events/conferences/search/index.html')

html = lxml.html.fromstring(link.text)
study = CSSSelector('div.content-r-full table.nogrid-nopad tr p>a[href]')
lines = study(html)
n=0
for line in lines:
    if n%3 == 0:
        print "Conference name: ",line.text
        print "============="
        n+=1
    elif n%3 ==1:
        print "Conference Date: ",line.text
        print "============="
        n+=1
    elif n%3 ==2:
        print "Location: ",line.text
        print "============="
        n+=1