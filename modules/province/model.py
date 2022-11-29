from config.database import db
from modules.country.model import CountryModel
from sqlalchemy import ForeignKey


class ProvinceModel(db.Model):
    __tablename__ = "province"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    idCountry = db.Column(
        db.Integer, ForeignKey(CountryModel.id), nullable=False
    )
