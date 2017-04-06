#coding: utf-8
import urllib2
request_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0)",
    "Accept": "text/html,application/xhtml+xml, */*",
    "Accept-Language": "en-US",
    "Connection": "keep-alive"
}
# FireFox 로 해결

request = urllib2.Request("http://www.example.com", headers=request_headers)
response = urllib2.urlopen(request)
html = response.read()
print html[:200]