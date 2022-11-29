from datetime import datetime, timedelta
import hashlib
import jwt
from config.database import db
from flask import Blueprint, jsonify, request, make_response, session
from modules.user.model import UserModel
from modules.user.repository import (
    find_user,
    find_users,
    find_exists_user,
)
from sqlalchemy import insert, update
import app

user_bp = Blueprint("user", __name__)


@user_bp.route("/register", methods=["POST"])
def add_user():
    """Function to add a user type."""
    data = request.json
    id_person = data["idPerson"]
    password = data["password"]
    users = find_users()
    for user in users:
        if id_person == user["idPerson"]:
            return (
                jsonify({"message": "Ya existe un usuario con esa persona"}),
                404,
            )
    data["password"] = hashlib.md5(password.encode("utf-8")).hexdigest()
    insert_db = insert(UserModel).values(data)
    db.session.execute(insert_db)
    db.session.commit()
    return (
        jsonify(
            {"message": "El usuario se creo correctamente"},
            {"data": id_person},
        ),
        201,
    )


@user_bp.route("/list", methods=["GET"])
def get_all_users():
    """Function to list all user types."""
    users = find_users()
    return jsonify({"data": users})


@user_bp.route("/<id>", methods=["GET"])
def get_user(id):
    """Function to get a userType."""
    exists = find_exists_user(id)
    if not exists:
        return jsonify({"message": "El usuario no existe"})
    userType = find_user(id)
    return jsonify({"data": userType})


@user_bp.route("/update", methods=["PUT"])
def update_user():
    """Function to update a userType."""
    data = request.json
    id = data["id"]
    exists = find_exists_user(id)
    if exists:
        update_db = (
            update(UserModel).where(UserModel.id == data["id"]).values(data)
        )
        db.session.execute(update_db)
        db.session.commit()
        return jsonify({"message": "El usuario se actualizo correctamente"})
    return jsonify({"message": "El usuario no existe"})


@user_bp.route("/login", methods=["GET"])
def login():
    auth = request.authorization
    username = auth["username"]
    password = auth["password"].encode("utf-8")
    if not auth or not auth.username or not auth.password:
        return make_response(
            {"Error": "No se enviaron todos lo parametros auth"}, 401
        )
    hasheada = hashlib.md5(password).hexdigest()
    print(hasheada)
    user_login = (
        db.session.query(UserModel)
        .filter_by(userName=username)
        .filter_by(password=hasheada)
        .first()
    )
    if user_login:
        token = jwt.encode(
            {
                "usuario": username,
                "id_usuario": user_login.id,
                "exp": datetime.utcnow() + timedelta(minutes=5),
            },
            app.app.secret_key,
        )
        session["api_session_token"] = token
        return jsonify({"Token": token.decode("UTF-8")})
    return make_response({"Error": "Algun dato no coincide"}, 401)


@user_bp.route("/logout", methods=["GET"])
def logout():
    session.pop("api_session_token", None)
    return jsonify({"message": "Sesion cerrada correctamente"})
