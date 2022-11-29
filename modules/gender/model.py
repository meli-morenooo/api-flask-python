from config.database import db


class GenderModel(db.Model):
    __tablename__ = 'gender'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    value = db.Column(db.String(3), nullable=False)
