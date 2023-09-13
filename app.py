from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://neilroberts@localhost:5432/pingpong"
db = SQLAlchemy(app)
from models.bat import Bat
from models.player import Player 

migrate = Migrate(app, db)

