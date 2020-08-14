from app import db

class subUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer,nullable=False)
    f_name = db.Column(db.String(50), index=True, nullable=False)
    l_name = db.Column(db.String(50), index=True, nullable=False)
