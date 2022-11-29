from config.database import db
from flask import Blueprint, jsonify, request
from modules.dni_type.model import DniTypeModel
from modules.dni_type.repository import (
    find_dni_types,
    find_dni_type,
    find_exists_dni_type,
)
from sqlalchemy import insert, update


dni_type_bp = Blueprint("dni_type", __name__)


@dni_type_bp.route("/register", methods=["POST"])
def add_dni_type():
    """Function to add a type of dni."""
    data = request.json
    name = data["name"]
    dni_types = find_dni_types()
    for dni_type in dni_types:
        if name == dni_type["name"]:
            return (
                jsonify(
                    {"message": "Ya existe un tipo de dni con ese nombre"}
                ),
                404,
            )
    insert_db = insert(DniTypeModel).values(data)
    db.session.execute(insert_db)
    db.session.commit()
    return (
        jsonify(
            {"message": "El tipo de dni se creo correctamente"},
            {"data": name},
        ),
        201,
    )


@dni_type_bp.route("/list", methods=["GET"])
def get_all_dni_type():
    """Function to list all dni types."""
    dni_types = find_dni_types()
    return jsonify({"data": dni_types})


@dni_type_bp.route("/<id>", methods=["GET"])
def get_dni_type(id):
    """Function to get a type dni."""
    exists = find_exists_dni_type(id)
    if not exists:
        return jsonify({"message": "El tipo de dni no existe"})
    dni_type = find_dni_type(id)
    return jsonify({"data": dni_type})


@dni_type_bp.route("/update", methods=["PUT"])
def update_dni_type():
    """Function to update a type of dni."""
    data = request.json
    id = data["id"]
    exists = find_exists_dni_type(id)
    if exists:
        update_db = (
            update(DniTypeModel)
            .where(DniTypeModel.id == data["id"])
            .values(data)
        )
        db.session.execute(update_db)
        db.session.commit()
        return jsonify(
            {"message": "El tipo de dni se actualizo correctamente"}
        )
    return jsonify({"message": "El tipo de dni no existe"})
