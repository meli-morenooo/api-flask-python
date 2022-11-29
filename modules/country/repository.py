"""Module for create repository for the country table."""
from config.database import db
from modules.country.model import CountryModel
from modules.country.schema import CountrySchema


def find_countries():
    """Function to find all countries."""
    query = db.session.query(CountryModel).all()
    schema = CountrySchema().dump(query, many=True)
    return schema


def find_country(id: str) -> dict:
    """Function to find a country."""
    query = db.session.query(CountryModel).filter(CountryModel.id == id).frst()
    schema = CountrySchema().dump(query, many=False)
    return schema


def find_exists_country(id: str) -> dict:
    """Function to find it exists a country."""
    query = (
        db.session.query(CountryModel).filter(CountryModel.id == id).count()
    )
    return query
