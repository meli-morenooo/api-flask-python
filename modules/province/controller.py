from config.database import db
from flask import Blueprint, jsonify, request
from modules.province.model import ProvinceModel
from modules.province.repository import (
    find_provinces,
    find_province,
    find_exists_province,
    find_provinces_country,
)
from modules.country.repository import find_exists_country
from sqlalchemy import insert, update


province_bp = Blueprint("province", __name__)


@province_bp.route("/register", methods=["POST"])
def add_gender():
    """Function to add a province."""
    data = request.json
    name = data["name"]
    id_country = data["id_country"]
    if not id_country:
        return jsonify({"message": "Debe ingresar un país"})
    exists_country = find_exists_country(id_country)
    if not exists_country:
        return jsonify({"message": "No existe el país"})
    provinces = find_provinces()
    for province in provinces:
        if name == province["name"] and id_country == province["id_country"]:
            msg = "Ya existe una provincia en este pais con ese nombre"
            return (
                jsonify({"message": msg}),
                404,
            )
    insert_db = insert(ProvinceModel).values(data)
    db.session.execute(insert_db)
    db.session.commit()
    return (
        jsonify(
            {"message": "La provincia se creo correctamente"},
            {"data": name},
        ),
        201,
    )


@province_bp.route("/list", methods=["GET"])
def get_all_provinces():
    """Function to list all provinces."""
    provinces = find_provinces_country()
    return jsonify({"data": provinces})


@province_bp.route("/<id>", methods=["GET"])
def get_province(id):
    """Function to get a province."""
    data = request.json
    id_country = data["id_country"]
    if not id_country:
        return jsonify({"message": "Debe ingresar un país"})
    exists_country = find_exists_country(id_country)
    if not exists_country:
        return jsonify({"message": "No existe el país"})
    exists = find_exists_province(id, data["id_country"])
    if not exists:
        return jsonify({"message": "El tipo de usuario no existe"})
    if not exists:
        return jsonify(
            {"message": "No existe una provincia en este pais con ese nombre"}
        )
    province = find_province(id, id_country)
    return jsonify({"data": province})


@province_bp.route("/update", methods=["PUT"])
def update_province():
    """Function to update a province."""
    data = request.json
    id = data["id"]
    id_country = data["id_country"]
    if not id_country:
        return jsonify({"message": "Debe ingresar un país"})
    exists_country = find_exists_country(id_country)
    if not exists_country:
        return jsonify({"message": "No existe el país"})
    exists = find_exists_province(id, id_country)
    if id_country:
        data.pop("id_country")
    if exists:
        update_db = (
            update(ProvinceModel)
            .where(ProvinceModel.id == data["id"])
            .values(data)
        )
        db.session.execute(update_db)
        db.session.commit()
        return jsonify({"message": "La provincia se actualizo correctamente"})
    return jsonify({"message": "La provincia no existe en ese país"})
