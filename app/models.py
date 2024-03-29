from app import app, db


class Fit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    done = db.Column(db.Boolean)
    error = db.Column(db.Text)
    filename = db.Column(db.Text)

    def status(self):
        if self.done:
            return 'OK'
        elif not self.error:
            return 'WAIT'
        else:
            return self.error
