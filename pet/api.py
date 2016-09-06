from flask.views import MethodView
from flask import jsonify, request, abort

from app.decorators import app_required

class PetAPI(MethodView):

    decorators = [app_required]

    def get(self, pet_id):
        if pet_id:
            return jsonify({"pet": self.pets[pet_id - 1]})
        else:
            return jsonify({"pets": self.pets})

    def post(self):
        if not request.json or not 'name' in request.json:
            abort(400)
        pet = {
            "id": len(self.pets) + 1,
            "name": request.json["name"],
            "location": "/pets/" + str(len(self.pets) + 1)
        }
        self.pets.append(pet)
        return jsonify({'pet': pet}), 201

    def put(self, pet_id):
        if not request.json or not 'name' in request.json:
            abort(400)
        pet = self.pets[pet_id - 1]
        pet["name"] = request.json["name"]
        return jsonify({'pet': pet}), 200

    def delete(self, pet_id):
        del self.pets[pet_id - 1]
        return jsonify({}), 204
