from config.database import db
from sqlalchemy import ForeignKey
from modules.user_type.model import UserTypeModel
from modules.person.model import PersonModel
from sqlalchemy.sql import func


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    idTypeUser = db.Column(
        db.Integer, ForeignKey(UserTypeModel.id), nullable=False
    )
    uploadDate = db.Column(
        db.TIMESTAMP, server_default=func.now(), nullable=True
    )
    idPerson = db.Column(
        db.Integer, ForeignKey(PersonModel.id), nullable=False
    )
