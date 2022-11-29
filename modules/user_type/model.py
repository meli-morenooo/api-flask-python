from config.database import db


class UserTypeModel(db.Model):
    __tablename__ = 'userType'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Integer, nullable=False)
