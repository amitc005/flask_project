from flask_restplus import Api
from flask import Blueprint

from .main.controller.assetlocation_controller import api as location_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='',
          version='1.0',
          description=''
          )

api.add_namespace(location_ns, path='/location')

