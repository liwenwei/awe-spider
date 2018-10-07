from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin

# url parse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result)

result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result)

result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')

# url unparse
data = ['http', 'www.baidu.com', 'index.html', 'user', 'id=6', 'comment']
print(urlunparse(data))

# url split
result = urlsplit('www.baidu.com/index.html;user?id=5#comment')
print(result)

# url unsplit
data = ['http', 'www.baidu.com', 'index.html', 'id=6', 'comment']
print(urlunsplit(data))

print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html’, 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com’, '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))