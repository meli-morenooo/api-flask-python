"""Database module, including the SQLAlchemy database object."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    """Function to initialize the database module."""
    db.init_app(app)
    with app.app_context():
        db.create_all()
