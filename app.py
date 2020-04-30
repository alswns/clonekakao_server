from flask import Flask,request,jsonify,abort
import pymongo
from pymongo import MongoClient
import re
import os
conn=MongoClient('localhost',27017)
db=conn['auth']
app = Flask(__name__,static_url_path='/static')
    


@app.route('/')
def index():
    return 'Hello Flask'
    
@app.route('/isregi')
def isRegi():
    auth=db['auth']
    phone=request.args.get('phone')
    print(phone)
    # regex = re.compile(r'(\d{3})-(\d{4}-\d{4})')
    # matchobj=regex.search(phone)
    # areaCode=matchobj.group(1)
    # num=matchobj.group(2)
    for i in auth.find({'phone':phone}):   
        return "true"
    return "false"


@app.route('/register',methods=['POST'])
def regiser():
    auth=db['auth']
    json=request.json
    print(request.form)
    print(request.files['image'])
    request.files['image']
    auth.insert({"name":request.form['name'],"image":  request.files['image'],"phone":request.form['name']})
    # print(request.form['image'])
    # print(request.form['image'])
    # phone=json['phone']
    # for i in auth.find({'phone':phone}):
    #     print('이미있는아이디입니다')
    #     return "used"
    # auth.insert(json)
    # print('회원가입성공')
    # return "complet"
    # print(json)
    return "good"
    # auth.insert()
@app.route('/auth',methods=['POST'])
def login():
    auth=db['auth']
    data=request.data.decode('utf-8')
    
    user=request.get_json()
    json=request.json
    print(json)
    phone=json['id']
    pw=json['pw']
    a=auth.find({'id':id})
    for i in a:
        print(i)
        if i['pw']==pw:
            return 'true'

    if id==None or pw==None:
        return None
    return 'false'

app.run(host='0.0.0.0',port=80, debug=True) 