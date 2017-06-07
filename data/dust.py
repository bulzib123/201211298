# coding: utf-8
import os
import requests
import urlparse
import mylib

def doIt():
    keyPath=os.path.join(os.getcwd()+'/key.properties')
    key=mylib.getKey(keyPath)
    # (1) make params with resource IDs
    KEY=key['dataseoul']
    TYPE='json'
    SERVICE='ForecastWarningMinuteParticleOfDustService'
    START_INDEX=str(1)
    END_INDEX=str(5)
    #LINE_NUM=str(2)
    params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX)
    # (2) make a full url
    _url='http://openAPI.seoul.go.kr:8088/'
    url=urlparse.urljoin(_url,params)
    url=url.replace('\\','/')
    # (3) get data
    data=requests.get(url).text
    print data

if __name__ == "__main__":
    doIt()