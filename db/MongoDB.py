import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.text  # 选择数据库
db = client['test']

# 指定集合
collection = db.students
collection = db['students']

# insert
# 实际上在 PyMongo 3.X 版本中，insert() 方法官方已经不推荐使用了，当然继续使用也没有什么问题，
# 官方推荐使用 insert_one() 和 insert_many() 方法将插入单条和多条记录分开
student1 = {
    'id': '20180001',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
result = collection.insert(student)
print(result)

# select
result = collection.find_one({'name': 'Mike'})
print(type(result))
print(result)

results = collection.find({'age': {'$gt': 20}})
results = collection.find({'name': {'$regex': '^M.*'}})

count = collection.find().count()
print(count)

# sort
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

# 偏移
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

# update
# 另外 update() 方法其实也是官方不推荐使用的方法，
# 在这里也分了 update_one() 方法和 update_many() 方法，用法更加严格，
# 第二个参数需要使用 $ 类型操作符作为字典的键名
condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
print(result)

# remove
result = collection.remove({'name': 'Kevin'})
print(result)
