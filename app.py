import json

from flask import Flask
from flask import request
from flask_cors import CORS
from flask_jwt import JWT

from database.MongodbManager import MongoManager
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'qazwsx'
CORS(app)

jwt = JWT(app, authenticate, identity)


@app.route('/orders', methods=['GET', 'POST'])
def save_order():
    if request.method == 'POST':
        order = json.loads(request.data)
        # Insert the data to DB
        MongoManager().save_order(order)
        return json.dumps({'success': True})

    if request.method == 'GET':
        return json.dumps(MongoManager().get_all_orders())


@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    ingredients = {
            'salad': 0,
            'bacon': 0,
            'cheese': 0,
            'meat': 0
            }
    return json.dumps(ingredients)


if __name__ == '__main__':
    app.run(port=3001)
