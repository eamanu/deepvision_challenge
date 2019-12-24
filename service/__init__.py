import os
from flask import Flask
from flask_restful import Api


def create_app(object_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(object_name)

    from service.api.v1.efemerides.api import efemerides_api
    from service.api.v1.efemerides.api import Efemerides

    api = Api(efemerides_api)

    api.add_resource(Efemerides, '/api/v1/efemerides')
    app.register_blueprint(efemerides_api)
    return app
