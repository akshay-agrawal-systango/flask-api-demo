import datetime

from flask import request, jsonify
from flask.views import MethodView


class UsersAPI(MethodView):
    def get(self, user_id):
        return jsonify({'user_id': user_id})

    def post(self):
        print("create new user in db")
        return jsonify({'id': '100'})

