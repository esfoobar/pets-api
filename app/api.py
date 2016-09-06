from flask.views import MethodView
from flask import request, abort, jsonify

from app.models import App, Access

class AppAPI(MethodView):

    def __init__(self):
        if not request.json:
            abort(400)

    def post(self):
        if not "app_id" in request.json or not "app_secret" in request.json:
            error = {
                "code": "MISSING_APP_ID_OR_APP_SECRET"
            }
            return jsonify({'error': error}), 400
        else:
            return jsonify({'result': 'ok'})
