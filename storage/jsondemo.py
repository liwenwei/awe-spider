import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('name'))
print(data[0].get('age'))  # None
print(data[0].get('age', 18))  # set default value

# read json file
with open('data.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)

# write json file
data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]

with open('data.json', 'w') as file:
    file.write(json.dumps(data))


# keep indent(保留Json格式）
with open('data.json', 'w') as file:
    file.write(json.dumps(data, indent=2))

# Unicode
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))