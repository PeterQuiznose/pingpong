from flask import Flask, render_template, request, redirect
from flask import Blueprint 
from models.player import Player
from models.bat import Bat
from app import db

bat_blueprint = Blueprint("bats", __name__)

@bat_blueprint.route("/bats")
def index():
    
    # player1 = Player(name="Darren", age=35, takes_it_seriously=False, ranking=3)
    # player2 = Player(name="Neil", age=38, takes_it_seriously=False, ranking=2)
    # player3 = Player(name="Robert from E65", age=30, takes_it_seriously=True, ranking=1)


    # db.session.add(player1)
    # db.session.add(player2)
    # db.session.add(player3)
   

    # bat1 = Bat(name="Red Bat", colour="red", smashability=3)
    # bat2 = Bat(name="The Black One", colour="black", smashability=5)
    # bat3 = Bat(name="The slicing, smashing super-dooper bat", colour="rainbow", smashability=10)

    # db.session.add(bat1)
    # db.session.add(bat2)
    # db.session.add(bat3)
    # db.session.commit()

    return render_template("bat_list.jinja")