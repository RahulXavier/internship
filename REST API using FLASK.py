# Author : Rahul Xavier
# POST and GET operation using Flask

from flask import jsonify,Flask,request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})


@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    data = "The number required is" + num
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(debug=True)

#curl http://127.0.0.1:5000/

#curl http://127.0.0.1:5000/home/10