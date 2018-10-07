import socket
import urllib.request
import urllib.parse
import urllib.error

url_get = 'http://httpbin.org/get'
url_post = 'http://httpbin.org/post'

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
req = urllib.request.Request(url=url_post, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))