from config.database import db
from modules.province.model import ProvinceModel
from sqlalchemy import ForeignKey


class LocationsModel(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    idProvince = db.Column(
        db.Integer, ForeignKey(ProvinceModel.id), nullable=False
    )
