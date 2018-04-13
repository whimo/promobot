from app import app, db

class Fit(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    done = db.Column(db.Boolean)
    filename = db.Column(db.Text)

    def status(self):
        return 'OK'

