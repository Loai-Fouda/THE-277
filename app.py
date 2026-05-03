#Flask
from flask import Flask, render_template, request, session, jsonify
import json
from game import HangmanGame

app = Flask(__name__)
app.secret_key = "hangman_secret_2026"   


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/new_game", methods=["POST"])
def new_game():
    
    game = HangmanGame()
    game_state = game.start_new_game()

    session["game_state"] = game_state
    return jsonify(game_state)

@app.route("/guess", methods=["POST"])

