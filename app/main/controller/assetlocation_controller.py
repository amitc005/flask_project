from flask import request, jsonify
from flask_restplus import Resource

from ..util.dto import LocationDTO

from ..service.assetlocation_service import save_location, update_location, delete_location, get_location_list

api = LocationDTO.api
_location = LocationDTO.assetlocation


@api.route('/')
class AssetLocation(Resource):
    @api.response(201, 'User successfully created.')
    @api.marshal_list_with(_location, envelope='data')
    @api.expect(_location, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_location(data=data)

    def put(self):
        """Creates a new User """
        data = request.json
        return update_location(data=data)

    def delete(self):
        """Creates a new User """
        data = request.json
        return delete_location(data=data)

@api.route('/getlocations/<int:per_page>/<int:page_num>')
class LocationList(Resource):
    def get(self, per_page, page_num):
        return jsonify(get_location_list(per_page, page_num))

