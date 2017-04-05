# coding: utf-8
import lxml.html
import requests
from lxml.cssselect import CSSSelector

keyword='비오는'
url = requests.get("http://music.naver.com/search/search.nhn?query=%EB%B9%84%EC%98%A4%EB%8A%94&target=track")
_html = lxml.html.fromstring(url.text)

sel = CSSSelector('table[summary] > tbody > ._tracklist_move')
nodes = sel(_html)

_selPopular = CSSSelector('.popular> div> span> em')
_selName = CSSSelector('.name > a.title')
_selArtist = CSSSelector('._artist.artist')
_selAlbum= CSSSelector('.album > a')
for node in nodes:
    _popular=_selPopular(node)
    _name=_selName(node)
    _artist=_selArtist(node)
    _album=_selAlbum(node)
    if _name:
        print _artist[0].text_content().strip(),
        print "---",
        print _name[0].text_content(),
        print "---",
        print _album[0].text_content(),
        print "---",
        print "인기", _popular[0].text_content()