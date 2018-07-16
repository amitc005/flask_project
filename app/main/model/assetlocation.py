from .. import db


class AssetLocation(db.Model):
    __tablename__ = "assetlocation"
    pri_id = db.Column(db.INTEGER, primary_key=True)
    id = db.Column(db.Integer)
    description = db.Column(db.VARCHAR(30))
    date_time = db.Column(db.TIMESTAMP)
    longitude = db.Column(db.DECIMAL(18,12))
    latitude = db.Column(db.DECIMAL(18,12))
    elevation = db.Column(db.INTEGER)

    def __init__(self, id, description, date_time, longtitude, latitude, elevation):
        self.id = id
        self.description = description
        self.date_time = date_time
        self.longitude = longtitude
        self.latitude = latitude
        self.elevation = elevation
