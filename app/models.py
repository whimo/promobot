from app import app, db

class Fit(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


