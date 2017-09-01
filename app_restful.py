from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity


app = Flask(__name__)
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    def get(self, name):
        ## Solution 1
        # for item in items:
        #     if item['name'] == name:
        #         return item

        ## item = list(filter(lambda x: x['name'] == name, items))[0]
        item = next(filter(lambda x: x['name'] == name, items), None)

        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message':'An item with name {} already exists.'.format(name)}, 400

        data = request.get_json()
        item = {'name': data['name'], 'price': float(data['price'])}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'times': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=9527, debug=True)
