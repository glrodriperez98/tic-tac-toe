
## ENTRY POINT REACT TO TALK TO GAME

from flask import Flask, jsonify, request
from flask_cors import CORS
from tic_tac_toe.game_logic import make_move, reset_game, get_game_state, reset_scores, coin_toss, set_starting_player

app = Flask(__name__)
CORS(app)

@app.route("/game-state", methods=["GET"])
def get_game():
    """Return the current game state to React."""
    return jsonify(get_game_state())

@app.route("/coin-toss", methods=["GET"])
def toss_coin():
    """API endpoint for coin toss."""
    winner = coin_toss()
    return jsonify({"winner": winner})

@app.route("/set-starting-player", methods=["POST"])
def set_starting_player_api():
    """Set the first player after the coin toss winner chooses X or O."""
    data = request.json
    chosen_marker = data.get("marker")
    set_starting_player(chosen_marker)
    return jsonify({"current_player": chosen_marker})

@app.route("/make-move", methods=["POST"])
def move():
    """Process a player's move."""
    data = request.json
    index = data.get("index")

    winner = make_move(index)
    return jsonify({"winner": winner, "state": get_game_state()})

@app.route("/reset", methods=["POST"])
def reset():
    """Reset the game state."""
    reset_game()
    return jsonify(get_game_state())

@app.route("/reset-scores",  methods=["POST"])
def reset_scores_api():
    """Reset player scores."""
    reset_scores()
    return jsonify(get_game_state())

if __name__ == "__main__":
    app.run(debug=True)
