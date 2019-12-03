from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add',methods=['POST'])
def add():
    dataDict = {}
    dataDict = request.get_json()

    x = dataDict['x']
    y = dataDict['y']
    z = x+y

    retjson = {
    'z':z
    }

    return jsonify(retjson), 200
@app.route('/')
def helloWorld():
    return 'Hello World'
@app.route('/hithere')
def hi_there():
        return 'Hi There'

@app.route('/bye')
def bye():
    c = 2*234
    retjson = {
    'name':'Prashant',
    'Age': 21,
    'Phones':[
    {
    'phoneName':'Nokia',
    'phoneNumber':222222
    },
    {
    'phoneName':'Honor',
    'phoneNumber':2343221
    }
    ]

    }
    return jsonify(retjson)


if __name__ == '__main__':
    app.run(DEBUG = True)
