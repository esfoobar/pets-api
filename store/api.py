from flask.views import MethodView
from flask import jsonify, request, abort, g
from jsonschema import Draft4Validator
from jsonschema.exceptions import best_match

from app.decorators import app_required
from store.models import Store
from store.schema import schema

class StoreAPI(MethodView):

    decorators = [app_required]

    def __init__(self):
        if request.method != 'GET' and not request.json:
            abort(400)

    def get(self, store_id):
        return jsonify({"stores": []}), 200

    def post(self):
        store_json = request.json
        error = best_match(Draft4Validator(schema).iter_errors(store_json)).message
        print(error)
        return jsonify({}), 200

    def put(self, pet_id):
        pass

    def delete(self, pet_id):
        pass
