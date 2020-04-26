from flask import Flask,request,jsonify
import pymongo
from pymongo import MongoClient
import json
conn=MongoClient('localhost',27017)
db=conn['auth']
app = Flask(__name__)
    


@app.route('/')
def index():
    return 'Hello Flask'
    
@app.route('/info')
def info():
    return 'Info'
@app.route('/auth',methods=['POST'])
def login():
    auth=db['auth']
    data=request.data.decode('utf-8')
    
    user=request.get_json()
    json=request.json
    id=json['id']
    pw=json['pw']
    a=auth.find({'id':id})
    for i in a:
        print(i)
        if i['pw']==pw:
            return '일치'

    if id==None or pw==None:
        return None
    return '불일치'

app.run(port=80, debug=True) 