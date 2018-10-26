import csv

# CSV is short for Comma-Sepatated Values(逗号分隔值或字符分隔值)

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerows([['10002', 'Bob', 45], ['10003', 'liwenwei', 18]])

# 但是一般情况下爬虫爬去的都是结构化数据，我们一般会用字典来表示
with open('data.csv', 'w', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 45})
    writer.writerow({'id': '10003', 'name': 'liwenwei', 'age': 18})

# read
with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
