"""Module for create repository for the dni type table."""
from config.database import db
from modules.dni_type.model import DniTypeModel
from modules.dni_type.schema import DniTypeSchema


def find_dni_types():
    """Function to find all dni types."""
    query = db.session.query(DniTypeModel).all()
    schema = DniTypeSchema().dump(query, many=True)
    return schema


def find_dni_type(id: str) -> dict:
    """Function to find a dni type."""
    query = (
        db.session.query(DniTypeModel).filter(DniTypeModel.id == id).first()
    )
    schema = DniTypeSchema().dump(query, many=False)
    return schema


def find_exists_dni_type(id: str) -> dict:
    """Function to find if exists a dni type."""
    query = (
        db.session.query(DniTypeModel).filter(DniTypeModel.id == id).count()
    )
    return query
