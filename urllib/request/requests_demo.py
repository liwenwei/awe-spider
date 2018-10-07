import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

r = requests.post('http://httpbin.org/post')
r = requests.put('http://httpbin.org/get')
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

# upload file
files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)

# cookies
r = requests.get('https://www.baidu.com/')
print(r.cookies)

for key, value in r.cookies.items():
    print(key + '=' + value)