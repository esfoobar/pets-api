from flask.views import MethodView
from flask import jsonify, request, abort, g
from jsonschema import Draft4Validator
from jsonschema.exceptions import best_match
import uuid
import json

from app.decorators import app_required
from pet.models import Pet
from pet.schema import schema
from pet.templates import pet_obj, pets_obj
from store.models import Store

class PetAPI(MethodView):

    decorators = [app_required]

    def __init__(self):
        self.PETS_PER_PAGE = 10
        if request.method != 'GET' and not request.json:
            abort(400)

    def get(self, pet_id):
        if pet_id:
            pet = Pet.objects.filter(external_id=pet_id, sold=False).first()
            if pet:
                response = {
                    "result": "ok",
                    "pet": pet_obj(pet)
                }
                return jsonify(response), 200
            else:
                return jsonify({}), 404
        else:
            pets = Pet.objects.filter(sold=False)
            page = int(request.args.get('page', 1))
            pets = pets.paginate(page=page, per_page=self.PETS_PER_PAGE)
            response = {
                "result": "ok",
                "links": [
                    {
                        "href": "/pets/?page=%s" % page,
                        "rel": "self"
                    }
                ],
                "pets": pets_obj(pets)
            }
            if pets.has_prev:
                response["links"].append(
                    {
                        "href": "/pets/?page=%s" % (pets.prev_num),
                        "rel": "previous"
                    }
                )
            if pets.has_next:
                response["links"].append(
                    {
                        "href": "/pets/?page=%s" % (pets.next_num),
                        "rel": "next"
                    }
                )
            return jsonify(response), 200

    def post(self):
        pet_json = request.json
        error = best_match(Draft4Validator(schema).iter_errors(pet_json))
        if error:
            return jsonify({"error": error.message}), 400

        store = Store.objects.filter(external_id=pet_json.get('store')).first()
        if not store:
            error = {
                "code": "STORE_NOT_FOUND"
            }
            return jsonify({'error': error}), 400
        else:
            pet = Pet(
                external_id=str(uuid.uuid4()),
                name=pet_json.get('name'),
                species=pet_json.get('species'),
                breed=pet_json.get('breed'),
                age=pet_json.get('age'),
                store=store,
                price=pet_json.get('price'),
                received_date=pet_json.get('received_date')
            ).save()
            response = {
                "result": "ok",
                "pet": pet_obj(pet)
            }
            return jsonify(response), 201

    def put(self, pet_id):
        pass

    def delete(self, pet_id):
        return jsonify({})
