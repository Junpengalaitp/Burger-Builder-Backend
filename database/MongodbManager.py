from pymongo import MongoClient


class MongoManager:
    def __init__(self):
        mongo_ip = '127.0.0.1'
        mongo_port = 27017
        db = 'Burger-Builder'
        client = MongoClient(f'mongodb://{mongo_ip}', int(mongo_port))
        database = client[db]
        self.collection = database['order']

    def save_order(self, order):
        self.collection.insert(order)

    def get_all_orders(self):
        orders = {}
        result = self.collection.find({})
        for order in result:
            print(order)
            orders[str(order['_id'])] = {key: value for key, value in order.items() if key != '_id'}
        print(orders)
        return orders


