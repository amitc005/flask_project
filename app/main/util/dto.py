from flask_restplus import Namespace, fields

class LocationDTO:
    api = Namespace('assetlocation', description='asset location record')
    assetlocation = api.model('assetlocation', {
        'pri_id' : fields.Integer,
        'id': fields.Integer(required=True),
        'description': fields.String(required=True),
        'date_time': fields.DateTime(required=True),
        'longitude': fields.Float(required=True, decimals=8),
        'latitude': fields.Float(required=True, decimals=8),
        'elevation': fields.Integer(required=True)

    })