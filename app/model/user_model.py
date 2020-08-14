from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), index=True, nullable=False)
    l_name = db.Column(db.String(50), index=True, nullable=False)
    street = db.Column(db.String(50), index=True, nullable=False)
    city = db.Column(db.String(50), index=True, nullable=False)
    state = db.Column(db.String(50), index=True, nullable=False)
    zip = db.Column(db.String(50), index=True, nullable=False)
