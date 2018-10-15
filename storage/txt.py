import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    title = item.find('h2').text()
    author = item.find('.author-link').text()
    answer = pq(item.find('.content').html()).text()
    with open('explore', 'a', encoding='utf-8') as file:
        file.write('\n'.join([title, author, answer]))
        file.write('\n' + '=' * 50 + '\n')
