import datetime
import dateutil.parser

import uuid
import datetime
import json
from app.main import db
from app.main.model.assetlocation import AssetLocation
from flask import jsonify


def save_location(data):
    try:
        new_location = AssetLocation(
            id=data['id'],
            description=data['description'],
            date_time=dateutil.parser.parse(data['date_time']),
            longtitude=data['longitude'],
            latitude=data['latitude'],
            elevation=data['elevation']
        )

        db.session.add(new_location)
        db.session.commit()
        return {'status': 'success', 'message': 'Successfully registered.'}, 201
    except Exception as error:
        return {"Error": "Server Error"}, 500


def update_location(data):
    try:
        asset_location = AssetLocation.query.filter_by(id=data['pri_id']).first()
        asset_location.id = data['id']
        asset_location.date_time = dateutil.parser.parse(data['date_time']),
        asset_location.description = data['description']
        asset_location.longitude = data['longitude']
        asset_location.latitude = data['latitude']
        asset_location.elevation = data['elevation']
        db.session.commit()
        return {"message": "update Succesfully"}, 201
    except Exception as error:
        return {"Error": "Server Error"}, 500


def delete_location(data):
    try:
        db.session.delete(AssetLocation.query.filter_by(data['pri_id']).first())
        db.session.commit()
    except Exception as error:
        return {"error": "unknown error"}, 500


def get_location_list(per_page, page_num):
    json_str_response = []
    try:
        lists = AssetLocation.query.paginate(per_page=per_page, page=page_num, error_out=True)
        for list in lists.items:
            json_str_response.append({
                'pri_id' : list.pri_id,
                'id' : list.id,
                'description' : list.description,
                'longitude' : str(list.longitude),
                'latitude' : str(list.latitude),
                'elevation' : str(list.elevation)
            })
        return json_str_response, 200
    except Exception as error:
        print(error)
        return {"error": "unknown error"}, 500
