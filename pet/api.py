from flask.views import MethodView
from flask import jsonify, request, abort, g

from app.decorators import app_required
from pet.models import Pet
from pet.templates import pet_obj, pets_obj

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
        pass

    def put(self, pet_id):
        pass

    def delete(self, pet_id):
        return jsonify({})
