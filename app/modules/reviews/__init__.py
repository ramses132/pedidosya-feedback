from app import api


def init_app(app, **kwargs):
    from . import models, resources
    api.add_namespace(resources.api)
