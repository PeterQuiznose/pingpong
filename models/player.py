from app import db

class Player (db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    takes_it_seriously = db.Column(db.Boolean)
    ranking = db.Column(db.Integer)
    bats = db.relationship('Bat', backref='player')

    def __repr__(self):
        return f"<Player: id: {self.id}, name: {self.name}, age: {self.age}, takes_it_seriously: {self.takes_it_seriously}, ranking:{self.ranking}>"