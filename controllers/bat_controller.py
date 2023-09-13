from flask import Flask, render_template, request, redirect
from flask import Blueprint 
from models.player import Player
from models.bat import Bat
from app import db

bat_blueprint = Blueprint("bats", __name__)

@bat_blueprint.route("/bats")
def show_bats():
    players_from_db = Player.query.all()
    bats_from_db = Bat.query.all()
    return render_template("bat_list.jinja", players=players_from_db, bats=bats_from_db)

@bat_blueprint.route("/bats/search")
def search():
    return render_template('search.jinja', title="Not a real search")

@bat_blueprint.route("/bats/contact")
def contact():
    return render_template('contact.jinja', title="Contact")

@bat_blueprint.route("/bats/<id>")
def show_one_bat(id):
    bat_to_show = Bat.query.get(id)
    return render_template("show_one_bat.jinja", bat=bat_to_show)

@bat_blueprint.route("/bats/delete/<id>", methods = ["POST"])
def delete_bat(id):
    bat_to_delete = Bat.query.get(id)
    if bat_to_delete:
        db.session.delete(bat_to_delete)
        db.session.commit()
        return redirect("/bats")

@bat_blueprint.route("/bats", methods=["POST"])
def save_bat():
    bat_name = request.form["name_of_bat"]
    bat_colour = request.form["colour"]
    bat_smashability = request.form["smashability"]
    player_of_bat = request.form["players"]

    bat_to_be_saved = Bat(name=bat_name, colour=bat_colour, smashability=bat_smashability, player_id=player_of_bat)
    db.session.add(bat_to_be_saved)
    db.session.commit()
    return redirect ("/bats")








    
    # player1 = Player(name="Darren", age=35, takes_it_seriously=False, ranking=3)
    # player2 = Player(name="Neil", age=38, takes_it_seriously=False, ranking=2)
    # player3 = Player(name="Robert from E65", age=30, takes_it_seriously=True, ranking=1)


    # db.session.add(player1)
    # db.session.add(player2)
    # db.session.add(player3)

    # db.session.commit()

    # bat1 = Bat(name="Red Bat", colour="red", smashability=3, player_id=player1.id)
    # bat2 = Bat(name="The Black One", colour="black", smashability=5)
    # bat3 = Bat(name="The slicing, smashing super-dooper bat", colour="rainbow", smashability=10)

    # db.session.add(bat1)
    # db.session.add(bat2)
    # db.session.add(bat3)
    # db.session.commit()
