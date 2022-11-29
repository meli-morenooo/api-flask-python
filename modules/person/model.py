from config.database import db
from sqlalchemy import ForeignKey
from modules.dni_type.model import DniTypeModel
from modules.locations.model import LocationsModel
from modules.gender.model import GenderModel
from sqlalchemy.sql import func


class PersonModel(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    idDniTypeUser = db.Column(db.Integer, ForeignKey(DniTypeModel.id))
    dni = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String(100), nullable=True)
    idLocation = db.Column(db.Integer, ForeignKey(LocationsModel.id))
    born = db.Column(db.TIMESTAMP, nullable=True)
    idGender = db.Column(db.Integer, ForeignKey(GenderModel.id))
    phone = db.Column(db.String(20), nullable=False)
    mail = db.Column(db.String(50), nullable=False)
    uploadDate = db.Column(
        db.TIMESTAMP, server_default=func.now(), nullable=True
    )
    active = db.Column(db.Boolean, nullable=True, default=True)
