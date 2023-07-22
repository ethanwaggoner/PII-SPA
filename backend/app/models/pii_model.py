from .database import db


class PiiModel(db.Model):
    __tablename__ = 'pii'

    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(100), nullable=False)
    pii_type = db.Column(db.String(100), nullable=False)
    pii_value = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.Date, nullable=False)
    is_false_positive = db.Column(db.Boolean, nullable=False)

    def __init__(self, hostname, pii_type, pii_value, file_path, timestamp, )