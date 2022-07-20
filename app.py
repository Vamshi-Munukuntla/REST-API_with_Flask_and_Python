from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My beautiful store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/')
def home():
    return render_template('index.html')

# POST  - used to receive data
# GET - used to send data back only


# POST /store data: {name}              # creates a new store with a given name.
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>              # get a store for given name and return some data about it.
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores
    # If the store name matches return it
    # if name does not match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /store                            # returns a list of all the stores.
@app.route('/store')
def get_store_all():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item        # creates an item inside the specific store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


# GET /store/<string:name>/item         # get all the items from a specific store
@app.route('/store/<string:name>/item')
def get_store_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)
