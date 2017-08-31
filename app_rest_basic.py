from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My store',
        'items': [
            {
                'name': 'book',
                'price': 15.99
            }
        ]
    }
]


# POST /store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()

    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/stores/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': float(request_data['price']),
            }
            store.items.append(new_item)

            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


@app.route('/stores/<string:name>/item')
def get_items_in_stores(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=9527)
