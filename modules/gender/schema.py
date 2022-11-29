from marshmallow import fields
from config.schema import ma


class GenderSchema(ma.Schema):
    """Schema for table gender."""
    id = fields.Integer(dump_only=True)
    name = fields.String()
    value = fields.String()
