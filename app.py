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
        return jsonify(isRegi=True)
    return jsonify(isRegi=False)

@app.route('/getImage')
def getImage():
    auth=db['auth']
    data=auth.find({"phone":"0104942613"})
    
    for i in data:
        print(i['image'])
        return jsonify(image=i['image'])
@app.route('/register',methods=['POST'])
def regiser():
    auth=db['auth']
    json=request.json
    print(request.form)
    try:
        auth.insert({"name":request.form['name'],"image":  request.form['image'],"phone":request.form['phone']})
        return jsonify(meseege="complet")
    except expression as identifier:
        return jsonify(meseege="failed")

    
    
    
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
            return jsonify(success=True,code=400,message="seccess")

    if id==None or pw==None:
        return jsonify(success=False,message="Id or Pw was Null",code=406)
    return jsonify(success=False,message="server error",code=500)

app.run(host='0.0.0.0',port=80, debug=True) 