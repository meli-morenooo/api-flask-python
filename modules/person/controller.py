from config.database import db
from flask import Blueprint, jsonify, request
from modules.person.model import PersonModel
from modules.person.repository import (
    find_person,
    find_persons,
    find_exists_person,
)
from sqlalchemy import insert, update


person_bp = Blueprint("person", __name__)


@person_bp.route("/register", methods=["POST"])
def add_person():
    """Function to add a user type."""
    data = request.json
    dni = data["dni"]
    persons = find_persons()
    for person in persons:
        print(person["dni"], dni)
        if int(dni) == int(person["dni"]):
            return (
                jsonify(
                    {"message": "Ya existe una persona con ese dni"}
                ),
                404,
            )
    insert_db = insert(PersonModel).values(data)
    db.session.execute(insert_db)
    db.session.commit()
    return (
        jsonify(
            {"message": "La persona se creo correctamente"},
            {"data": dni},
        ),
        201,
    )


@person_bp.route("/list", methods=["GET"])
def get_all_persons():
    """Function to list all user types."""
    persons = find_persons()
    return jsonify({"data": persons})


@person_bp.route("/<id>", methods=["GET"])
def get_person(id):
    """Function to get a person."""
    exists = find_exists_person(id)
    if not exists:
        return jsonify({"message": "El tipo de usuario no existe"})
    person = find_person(id)
    return jsonify({"data": person})


@person_bp.route("/update", methods=["PUT"])
def update_person():
    """Function to update a person."""
    data = request.json
    id = data["id"]
    exists = find_exists_person(id)
    if exists:
        print(data)
        data = dict(filter(lambda item: item[1], data.items()))
        update_db = (
            update(PersonModel)
            .where(PersonModel.id == data["id"])
            .values(data)
        )
        db.session.execute(update_db)
        db.session.commit()
        return jsonify(
            {"message": "La persona se actualizo correctamente"}
        )
    return jsonify({"message": "La persona no existe"})
