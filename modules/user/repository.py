from config.database import db
from modules.user.model import UserModel
from modules.person.model import PersonModel
from modules.user_type.model import UserTypeModel
from modules.user.schema import UserSchema, UserPasswordSchema


def find_users():
    """Function to find all users."""
    query = (
        db.session.query(
            UserModel.id,
            UserModel.userName,
            UserTypeModel.id.label("idTypeUser"),
            UserTypeModel.name.label("type_user_name"),
            UserModel.uploadDate,
            PersonModel.id.label("idPerson"),
            PersonModel.name.label("person_name"),
        )
        .join(PersonModel, UserModel.idPerson == PersonModel.id)
        .join(UserTypeModel, UserModel.idTypeUser == UserTypeModel.id)
        .all()
    )
    schema = UserSchema().dump(query, many=True)
    return schema


def find_user(id: str) -> dict:
    """Function to find a user."""
    query = (
        db.session.query(
            UserModel.id,
            UserModel.userName,
            UserTypeModel.id.label("idTypeUser"),
            UserTypeModel.name.label("type_user_name"),
            UserModel.uploadDate,
            PersonModel.id.label("idPerson"),
            PersonModel.name.label("person_name"),
        )
        .join(PersonModel, UserModel.idPerson == PersonModel.id)
        .join(UserTypeModel, UserModel.idTypeUser == UserTypeModel.id)
        .first()
    )
    schema = UserSchema().dump(query, many=False)
    return schema


def find_user_password(id: str) -> dict:
    """Function to find a user."""
    query = db.session.query(UserModel).filter(UserModel.id == id).first()
    schema = UserPasswordSchema().dump(query, many=False)
    return schema


def find_exists_user(id: str) -> dict:
    """Function to find if exists user."""
    query = db.session.query(UserModel).filter(UserModel.id == id).count()
    return query
