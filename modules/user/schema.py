from marshmallow import fields
from config.schema import ma


class UserSchema(ma.Schema):
    """Schema for table user."""
    id = fields.Integer(dump_only=True)
    idTypeUser = fields.Integer(attribute="idTypeUser")
    typeUserName = fields.String(attribute="type_user_name")
    uploadDate = fields.DateTime(attribute="uploadDate")
    idPerson = fields.Integer(attribute="idPerson")
    person_name = fields.String(attribute="person_name")
    userName = fields.String(attribute="userName")


class UserPasswordSchema(ma.Schema):
    """Schema for table user"""
    id = fields.Integer(dump_only=True)
    password = fields.String()
