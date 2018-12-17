from flask import Blueprint

from app import api


def init_app(app, *kwargs):

    api_v1_blueprints = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(api_v1_blueprints)
    app.register_blueprint(api_v1_blueprints)

