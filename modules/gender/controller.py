from config.database import db
from flask import Blueprint, jsonify, request
from modules.gender.model import GenderModel
from modules.gender.repository import (
    find_genders,
    find_gender,
    find_exists_gender,
)
from sqlalchemy import insert, update


gender_bp = Blueprint("gender", __name__)


@gender_bp.route("/register", methods=["POST"])
def add_gender():
    """Function to add a gender."""
    data = request.json
    name = data["name"]
    genders = find_genders()
    for gender in genders:
        if name == gender["name"]:
            return (
                jsonify({"message": "Ya existe un género con ese nombre"}),
                404,
            )
    insert_db = insert(GenderModel).values(data)
    db.session.execute(insert_db)
    db.session.commit()
    return (
        jsonify(
            {"message": "El género se creo correctamente"},
            {"data": name},
        ),
        201,
    )


@gender_bp.route("/list", methods=["GET"])
def get_all_genders():
    """Function to list all genders."""
    genders = find_genders()
    return jsonify({"data": genders})


@gender_bp.route("/<id>", methods=["GET"])
def get_gender(id):
    """Function to get a gender."""
    exists = find_exists_gender(id)
    if not exists:
        return jsonify({"message": "El género no existe"})
    gender = find_gender(id)
    return jsonify({"data": gender})


@gender_bp.route("/update", methods=["PUT"])
def update_gender():
    """Function to update a gender."""
    data = request.json
    id = data["id"]
    exists = find_exists_gender(id)
    if exists:
        update_db = (
            update(GenderModel)
            .where(GenderModel.id == data["id"])
            .values(data)
        )
        db.session.execute(update_db)
        db.session.commit()
        return jsonify({"message": "El género se actualizo correctamente"})
    return jsonify({"message": "El género no existe"})
