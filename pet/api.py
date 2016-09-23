from flask.views import MethodView
from flask import jsonify, request, abort, g

from app.decorators import app_required
from pet.models import Pet

class PetAPI(MethodView):

    decorators = [app_required]

    def __init__(self):
        if request.method != 'GET' and not request.json:
            abort(400)

    def get(self, pet_id):
        return jsonify({"pets": []}), 200

    def post(self):
        pass

    def put(self, pet_id):
        pass

    def delete(self, pet_id):
        return jsonify({})
