from marshmallow import fields
from config.schema import ma


class DniTypeSchema(ma.Schema):
    """Schema for table dniType."""
    id = fields.Integer(dump_only=True)
    name = fields.String()
