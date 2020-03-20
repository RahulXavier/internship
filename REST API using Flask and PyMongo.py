from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/RahulDB'

mongo = PyMongo(app)

@app.route('/add',methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']

    if _name and request.method=='POST' :
        id = mongo.db.Collection.insert({'name':_name})
        resp = jsonify('User added successfully')
        resp.status_code = 200
        return resp
    else: return not_found()

@app.route('/users')
def users():
    users = mongo.db.Collection.find()
    resp = dumps(users)
    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {'status':404, 'message':'Not found'+request.url}
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == '__main__':
    app.run(debug=True)