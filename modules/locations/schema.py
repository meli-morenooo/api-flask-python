from marshmallow import fields
from config.schema import ma


class LocationsSchema(ma.Schema):
    """Schema for table locations."""

    id = fields.Integer(dump_only=True, attribute="id")
    name_location = fields.String(attribute="name")
    idProvince = fields.Integer(attribute="idProvince")
    name_province = fields.String(attribute="province_name")
    idCountry = fields.Integer(attribute="idCountry")
    name_country = fields.String(attribute="country_name")
