from config.database import db


class CountryModel(db.Model):
    """Create a Country table."""
    __tablename__ = 'country'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return self.name

    def __init__(self, name):
        self.name = name
