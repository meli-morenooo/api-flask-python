from marshmallow import fields
from config.schema import ma


class CountrySchema(ma.Schema):
    """Schema for table country."""
    id = fields.Integer(dump_only=True)
    name = fields.String()
