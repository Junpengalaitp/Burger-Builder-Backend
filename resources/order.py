import json

from flask import make_response
from flask_restful import Resource, reqparse

from database.MongodbManager import MongoManager


class Order(Resource):
    parser = reqparse.RequestParser()

    def post(self, order):
        try:
            MongoManager().save_order(order)
        except:
            return {"message": "An error occurred inserting the item."}, 500  # Internal Server Error
        resp = make_response(json.dumps(order), 201)
        return resp


