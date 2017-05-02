import os
import src.mylib
import requests
keyPath=os.path.join(os.getcwd(),'src','key.properties')
key=src.mylib.getKey(keyPath)
_key=str(key['dataseoul'])
_url='http://openAPI.seoul.go.kr:8088'
_type='xml'
_service='CardSubwayStatsNew'
_start_index=1
_end_index=5
_use_mon='20151101'
_api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)
_api="http://openAPI.seoul.go.kr:8088/455447476562616734367662765444/xml/CardSubwayStatsNew/1/5/20151101"
_maxIter=2
_iter=0
while _iter<_maxIter:
    response = requests.get(_api).text
    print response
    _start_index+=5
    _end_index+=5
    _iter+=1