"""Database module, including the SQLAlchemy database object."""
from flask_marshmallow import Marshmallow

ma = Marshmallow()


def init_app(app):
    """Function to initialize the database module."""
    ma.init_app(app)
