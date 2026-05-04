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



def guess():

    game_state = session.get("game_state")
    if not game_state:
        return jsonify({"error": "No active game. Start a new game first."}), 400

    data = request.get_json()
    letter = data.get("letter", "").upper()

 
    if not letter or len(letter) != 1 or not letter.isalpha():
        return jsonify({"error": "Invalid letter. Please send a single alphabet character."}), 400

   
    game = HangmanGame()
    updated_state = game.process_guess(game_state, letter)

   
    session["game_state"] = updated_state
    return jsonify(updated_state)