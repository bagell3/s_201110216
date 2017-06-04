
import os
import requests
import re
import pprint



class MyPrettyPrinter(pprint.PrettyPrinter):
	def format(self, _object, context, maxlevels, level):
		if isinstance(_object, unicode):
			return "'%s'" % _object.encode('utf8'), True, False
		elif isinstance(_object, str):
			_object = unicode(_object,'utf8')
			return "'%s'" % _object.encode('utf8'), True, False
		return pprint.PrettyPrinter.format(self, _object, context, maxlevels, level)

APT='http://data.suwon.go.kr/suwon/openapi/service/getDataList.api?serviceId=aptjw&&pageNo=2&startDate=2011&endDate=2011&serviceKey=d0d29eb681434f339ee9a73664baef1f170417223236'

data=requests.get(APT).text

p=re.compile('<excluArea>(.+?)</excluArea>')
res=p.findall(data)

q=re.compile('<insurValue>(.+?)</insurValue>')
respon=q.findall(data)

r=re.compile('<bjdong>(.+?)</bjdong>')
BJdong=r.findall(data)

area=[]
price=[]
dong=[]

for item in res:
    x=item
    x=x.encode('raw_unicode_escape')
    area.append(x)
for item1 in respon:
    y=item1
    y=y.encode('raw_unicode_escape')
    price.append(y)
for item2 in BJdong:
    z=item2
    dong.append(z)
    
print area
print price
print MyPrettyPrinter().pformat(dong)