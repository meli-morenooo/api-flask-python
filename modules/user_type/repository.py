"""Module for create repository for the dni type table."""
from config.database import db
from modules.user_type.model import UserTypeModel
from modules.user_type.schema import UserTypeSchema


def find_user_types():
    """Function to find all user types."""
    query = db.session.query(UserTypeModel).all()
    schema = UserTypeSchema().dump(query, many=True)
    return schema


def find_user_type(id: str) -> dict:
    """Function to find a User Type."""
    query = (
        db.session.query(UserTypeModel).filter(UserTypeModel.id == id).first()
    )
    schema = UserTypeSchema().dump(query, many=False)
    return schema


def find_exists_user_type(id: str) -> dict:
    """Function to find if exists User Type."""
    query = (
        db.session.query(UserTypeModel).filter(UserTypeModel.id == id).count()
    )
    return query
