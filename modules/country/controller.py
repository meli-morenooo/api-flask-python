from config.database import db
from flask import Blueprint, jsonify, request
from modules.country.model import CountryModel
from modules.country.repository import (
    find_countries,
    find_country,
    find_exists_country,
)
from sqlalchemy import insert, update

country_bp = Blueprint("country", __name__)


@country_bp.route("/register", methods=["POST"])
def add_country():
    """Function to add a country."""
    data = request.json
    name = data["name"]
    countries = find_countries()
    for country in countries:
        if name == country["name"]:
            return (
                jsonify({"message": "Ya existe un país con ese nombre"}),
                404,
            )
    insert_db = insert(CountryModel).values(data)
    db.session.execute(insert_db)
    db.session.commit()
    return (
        jsonify(
            {"message": "El país se creo correctamente"},
            {"data": name},
        ),
        201,
    )


@country_bp.route("/list", methods=["GET"])
def get_all_countries():
    """Function to list all countries."""
    countries = find_countries()
    return jsonify({"data": countries})


@country_bp.route("/<id>", methods=["GET"])
def get_country(id):
    """Function to get a country."""
    exists = find_exists_country(id)
    if not exists:
        return jsonify({"message": "El país no existe"})
    country = find_country(id)
    return jsonify({"data": country})


@country_bp.route("/update", methods=["PUT"])
def update_country():
    """Function to update a country."""
    data = request.json
    id = data["id"]
    exists = find_exists_country(id)
    if exists:
        update_db = (
            update(CountryModel)
            .where(CountryModel.id == data["id"])
            .values(data)
        )
        db.session.execute(update_db)
        db.session.commit()
        return jsonify({"message": "El país se actualizo correctamente"})
    return jsonify({"message": "El país no existe"})
