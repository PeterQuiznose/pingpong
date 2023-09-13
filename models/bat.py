from app import db

class Bat (db.Model):
    __tablename__ = "bats"
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(64))
    colour = db.Column(db.String(64))
    smashability = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
  
def __repr__(self):
    return f"<Bat: id: {self.id}, name: {self.name}, colour: {self.colour}, smashability: {self.smashability}, player_id:{self.player.id}>"
    

