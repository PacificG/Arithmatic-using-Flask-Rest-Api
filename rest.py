from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(posted_data,function):
    if function == 'add' or function == 'subtract' or function == 'multiply':
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        else:
            return 200
    elif function == 'divide':
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        elif int(posted_data["y"])==0:
            return 302
        else:
            return 200


class Add(Resource):
    def post(self):

        posted_data = request.get_json(force = True)

        status_code = checkPostedData(posted_data,'add')
        if status_code != 200:
            retJson = {
            'message':'An error occured',
            'code':301
            }
            return jsonify(retJson)
        else:
            x = posted_data['x']
            y = posted_data['y']
            x = int(x)
            y = int(y)
            ret = x + y

            retMap = {
            'Message': ret,
            'Status code': 200
            }
            return jsonify(retMap)

class subtract(Resource):
    def post(self):

        posted_data = request.get_json(force = True)

        status_code = checkPostedData(posted_data,'subtract')
        if status_code != 200:
            retJson = {
            'message':'An error occured',
            'code':301
            }
            return jsonify(retJson)
        else:
            x = posted_data['x']
            y = posted_data['y']
            x = int(x)
            y = int(y)
            ret = x - y

            retMap = {
            'Message': ret,
            'Status code': 200
            }
            return jsonify(retMap)


class multiply(Resource):
    def post(self):

        posted_data = request.get_json(force = True)

        status_code = checkPostedData(posted_data,'multiply')
        if status_code != 200:
            retJson = {
            'message':'An error occured',
            'code':301
            }
            return jsonify(retJson)
        else:
            x = posted_data['x']
            y = posted_data['y']
            x = int(x)
            y = int(y)
            ret = x * y

            retMap = {
            'Message': ret,
            'Status code': 200
            }
            return jsonify(retMap)


class divide(Resource):
    def post(self):

        posted_data = request.get_json(force = True)

        status_code = checkPostedData(posted_data,'divide')
        if status_code != 200:
            if status_code == 301:
                retJson = {
                'message':'An error occured',
                'code':301
                }
                return jsonify(retJson)
            elif status_code == 302:
                retJson = {
                'message':'An error occured',
                'code':302
                }
                return jsonify(retJson)
        else:
            x = posted_data['x']
            y = posted_data['y']
            x = int(x)
            y = int(y)
            ret = x / y

            retMap = {
            'Message': ret,
            'Status code': 200
            }
            return jsonify(retMap)



api.add_resource(Add, '/add')
api.add_resource(subtract, '/subtract')
api.add_resource(multiply, '/multiply')
api.add_resource(divide, '/divide')


@app.route('/')
def Hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    app.run(debug=True)
