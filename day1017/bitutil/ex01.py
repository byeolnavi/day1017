from pymongo import MongoClient
from bson.json_util import dumps

import pprint

client = MongoClient('localhost', 27017)
mydb = client.bit
students = mydb.student

mydoc = {"name":"홍길동","age":20}
print(mydoc)
#s = {"name":"김슬지","kor":100, "eng":80, "math":90}
#mycol.insert_one(s)
#print(s)

#연습) 모든 학생의 이름, 국어, 영어, 수학을 출력
#for col in mycol.find():
#    pprint.pprint(col)

#연습) 국어점수가 80점이상인 학생의 이름과 국어점수를 출력
#for arr in mycol.find({'kor':{'$gt':80}},{'name':1, 'kor':1, '_id':0}):
#    pprint.pprint(arr)
arr = students.find({'kor':{'$gt':80}},{'name':1, 'kor':1, '_id':0})
r = dumps(arr, ensure_ascii=False)
print(r)
