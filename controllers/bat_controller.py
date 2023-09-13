from flask import Flask, render_template, request, redirect
from flask import Blueprint 
from models.player import Player
from models.bat import Bat
from app import db

bat_blueprint = Blueprint("bats", __name__)

