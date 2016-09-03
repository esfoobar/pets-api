from flask.views import MethodView

class PetAPI(MethodView):

    def get(self):
        return "Pet Get"

    def post(self):
        return "Pet Post"
