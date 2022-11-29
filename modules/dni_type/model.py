from config.database import db


class DniTypeModel(db.Model):
    __tablename__ = 'dniType'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=True)
