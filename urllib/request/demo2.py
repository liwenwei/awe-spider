import requests

r = requests.post('http://httpbin.org/post')
r = requests.put('http://httpbin.org/get')
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')