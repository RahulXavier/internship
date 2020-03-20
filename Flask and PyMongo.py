from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'RahulDB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/'

mongo = PyMongo(app)

@app.route('/framework',methods=['GET'])
def get_all_frameworks():
    frameworks = mongo.db.framework

    output = []
    for q in frameworks.find():
        output.append({ 'name':q['name']})
    return jsonify({'result':output})


if __name__ == '__main__':
    app.run(debug=True)