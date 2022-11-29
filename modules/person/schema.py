from marshmallow import fields
from config.schema import ma


class PersonSchema(ma.Schema):
    """Schema for table gender."""

    idPerson = fields.Integer(dump_only=True, attribute="id")
    namePerson = fields.String(attribute="name")
    idDniType = fields.Integer(attribute="id_dni_type")
    dniTypeName = fields.String(attribute="dni_type_name")
    dni = fields.String(attribute="dni")
    address = fields.String(attribute="address")
    idLocation = fields.Integer(attribute="id_location")
    location_name = fields.String(attribute="location_name")
    idProvince = fields.Integer(attribute="id_province")
    province_name = fields.String(attribute="province_name")
    idCountry = fields.Integer(attribute="id_country")
    country_name = fields.String(attribute="country_name")
    born = fields.Date(attribute="born")
    idGender = fields.Integer(attribute="id_gender")
    gender_name = fields.String(attribute="gender_name")
    phone = fields.String(attribute="phone")
    mail = fields.String(attribute="mail")
    uploadDate = fields.DateTime(attribute="uploadDate")
    active = fields.Boolean(attribute="active")
