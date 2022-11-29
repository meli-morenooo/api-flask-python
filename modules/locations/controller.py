from config.database import db
from flask import Blueprint, jsonify, request
from modules.locations.model import LocationsModel
from modules.locations.repository import (
    find_exists_location,
    find_location,
    find_locations,
)
from modules.province.repository import find_exists_province
from sqlalchemy import insert, update

locations_bp = Blueprint("locations", __name__)


@locations_bp.route("/register", methods=["POST"])
def add_location():
    """Function to add a localidad."""
    data = request.json
    name = data["name"]
    id_province = data["idProvince"]
    id_country = data["idCountry"]
    data.pop("idCountry")
    if not id_province:
        return jsonify({"message": "Debe ingresar una provincia"})
    if not id_country:
        return jsonify({"message": "Debe ingresar una país"})
    exists_province = find_exists_province(
        id=id_province, idCountry=id_country
    )
    if not exists_province:
        return jsonify({"message": "No existe la provincia"})
    locations = find_locations()
    for location in locations:
        if (
            name == location["name_location"]
            and id_province == location["idProvince"]
            and id_country == location["idCountry"]
        ):
            msg = "Ya existe una localidad en esta provincia "
            msg += "y país con ese nombre"
            return (
                jsonify({"message": msg}),
                404,
            )
    insert_db = insert(LocationsModel).values(data)
    db.session.execute(insert_db)
    db.session.commit()
    return (
        jsonify(
            {"message": "La localidad se creo correctamente"},
            {"data": name},
        ),
        201,
    )


@locations_bp.route("/list", methods=["GET"])
def get_all_location():
    """Function to list all localidades."""
    locations = find_locations()
    return jsonify({"data": locations})


@locations_bp.route("/<id>", methods=["GET"])
def get_location(id):
    data = request.json
    id_province = data["idProvince"]
    id_country = data["idCountry"]
    if not id_province:
        return jsonify({"message": "Debe ingresar una provincia"})
    if not id_country:
        return jsonify({"message": "Debe ingresar un país"})
    exists_province = find_exists_province(
        id=id_province, idCountry=id_country
    )
    if not exists_province:
        return jsonify({"message": "No existe la provincia en ese país"})
    exists_location = find_exists_location(id, id_province)
    if not exists_location:
        return jsonify({"message": "No existe la localidad en esta provincia"})
    location = find_location(id=id, idProvince=id_province)
    return jsonify({"data": location})


@locations_bp.route("/update", methods=["PUT"])
def update_location():
    """Function to update a locations."""
    data = request.json
    name = data["name"]
    id_location = data["id"]
    id_province = data["idProvince"]
    id_country = data["idCountry"]
    id_new_id_province = data["new_idProvince"]
    if not id_province:
        return jsonify({"message": "Debe ingresar una provincia"})
    if not id_country:
        return jsonify({"message": "Debe ingresar un país"})
    exists_province = find_exists_province(id_province, id_country)
    if not exists_province:
        msg = "No existe la localidad en de esa provincia en ese país"
        return jsonify({"message": msg})
    if id_new_id_province:
        data["idProvince"] = id_new_id_province
    else:
        data.pop("idProvince")
    data.pop("idCountry")
    data.pop("new_idProvince")
    data.pop("id")
    exists_location = find_exists_location(id_location, id_province)
    if not exists_location:
        return jsonify({"message": "No existe la localidad en esta provincia"})
    locations = find_locations()
    for location in locations:
        if (
            name == location["name_location"]
            and id_province == location["idProvince"]
            and id_country == location["idCountry"]
        ):
            msg = "Ya existe una localidad en esa provincia y "
            msg += "país con ese nombre"
            return jsonify({"message": msg}), 404
    if not name:
        name = location["name_location"]
        data.pop("name")
    update_db = (
        update(LocationsModel)
        .where(LocationsModel.id == id_location)
        .values(data)
    )
    db.session.execute(update_db)
    db.session.commit()
    return jsonify(
        {"message": "La localidad se actualizo correctamente"},
        {"data": name},
    )
