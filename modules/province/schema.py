from marshmallow import fields
from config.schema import ma


class ProvinceSchema(ma.Schema):
    """Schema for table province."""
    id = fields.Integer(dump_only=True)
    name = fields.String()
    idCountry = fields.Integer()


class ProvinceCountrySchema(ma.Schema):
    """Schema for table province."""
    id = fields.Integer(dump_only=True, attribute="idProvince")
    name_province = fields.String(attribute="province_name")
    idCountry = fields.Integer(attribute="idCountry")
    name_country = fields.String(attribute="country_name")
