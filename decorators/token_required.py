import jwt
from functools import wraps
from flask import request, jsonify
from modules.user.model import UserModel
import app


def token_required(f):
    @wraps
    def decorated(*args, **kwargs):
        token = None
        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:
            return jsonify({"ERROR": "Token is missing"}), 401
        try:
            datatoken = jwt.decode(token, app.app.secret_key)
            print(datatoken)
            userLogged = UserModel.query.filter_by(
                id=datatoken["id_usuario"]
            ).first()
        except:
            return jsonify({"ERROR": "Token is invalid or expired"}), 401
        return f(userLogged, *args, **kwargs)

    return decorated
