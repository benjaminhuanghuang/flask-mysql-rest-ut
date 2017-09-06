from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}