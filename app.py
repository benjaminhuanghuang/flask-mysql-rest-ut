from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
#
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item
from resources.items import ItemList
from resources.store import Store, StoreList

from db import db

def create_app(**config_overrides):
    app = Flask(__name__)
    app.secret_key = "SeCreT"

    app.config.from_pyfile('settings.py')
    app.config.update(config_overrides)


    db.init_app(app)

    api = Api(app)
    jwt = JWT(app, authenticate, identity)

    api.add_resource(Store, '/store/<string:name>')
    api.add_resource(StoreList, '/stores')
    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(UserRegister, '/register')


    @app.before_first_request()
    def create_tables():
        db.create_all()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
