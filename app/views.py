from flask import Blueprint

from app.api import AppAPI

app_app = Blueprint('app_app', __name__)

app_view = AppAPI.as_view('app_api')
app_app.add_url_rule('/apps/access/', view_func=app_view, methods=['POST',])
