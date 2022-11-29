from config.database import db
from flask import Blueprint, jsonify, request
from modules.user_type.model import UserTypeModel
from modules.user_type.repository import (
    find_user_types,
    find_user_type,
    find_exists_user_type,
)
from sqlalchemy import insert, update


user_type_bp = Blueprint("user_type", __name__)


@user_type_bp.route("/register", methods=["POST"])
def add_user_type():
    """Function to add a user type."""
    data = request.json
    name = data["name"]
    user_types = find_user_types()
    for user_type in user_types:
        print(user_type["name"])
        if name == user_type["name"]:
            return (
                jsonify(
                    {"message": "Ya existe un tipo de usuario con ese nombre"}
                ),
                404,
            )
    insert_db = insert(UserTypeModel).values(data)
    db.session.execute(insert_db)
    db.session.commit()
    return (
        jsonify(
            {"message": "El tipo de usuario se creo correctamente"},
            {"data": name},
        ),
        201,
    )


@user_type_bp.route("/list", methods=["GET"])
def get_all_user_types():
    """Function to list all user types."""
    user_types = find_user_types()
    return jsonify({"data": user_types})


@user_type_bp.route("/<id>", methods=["GET"])
def get_user_type(id):
    """Function to get a userType."""
    exists = find_exists_user_type(id)
    if not exists:
        return jsonify({"message": "El tipo de usuario no existe"})
    userType = find_user_type(id)
    return jsonify({"data": userType})


@user_type_bp.route("/update", methods=["PUT"])
def update_user_type():
    """Function to update a userType."""
    data = request.json
    id = data["id"]
    exists = find_exists_user_type(id)
    if exists:
        update_db = (
            update(UserTypeModel)
            .where(UserTypeModel.id == data["id"])
            .values(data)
        )
        db.session.execute(update_db)
        db.session.commit()
        return jsonify(
            {"message": "El tipo de usuario se actualizo correctamente"}
        )
    return jsonify({"message": "El tipo de usuario no existe"})
