"""Module for create repository for the dni type table."""
from config.database import db
from modules.gender.model import GenderModel
from modules.gender.schema import GenderSchema


def find_genders():
    """Function to find all genders."""
    query = db.session.query(GenderModel).all()
    schema = GenderSchema().dump(query, many=True)
    return schema


def find_gender(id: str) -> dict:
    """Function to find a gender."""
    query = db.session.query(GenderModel).filter(GenderModel.id == id).first()
    schema = GenderSchema().dump(query, many=False)
    return schema


def find_exists_gender(id: str) -> dict:
    """Function to find if exists gender."""
    query = db.session.query(GenderModel).filter(GenderModel.id == id).count()
    return query
