## GAME CONTROL AND LOGIC
import random

WINNING_COMBINATIONS = [
	[0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
	[0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
	[0, 4, 8], [2, 4, 6]			 # Diagonals
]

game_state = {
	"board": [" "] * 9,
	"current_player": "X",
	"winner": None,
	"scores": {"X": 0, "O": 0}
}

def check_winner():
	"""Check for a winner and update game state."""
	for combo in WINNING_COMBINATIONS:
		if game_state["board"][combo[0]] == game_state["board"][combo[1]] == game_state["board"][combo[2]] != " ":
			game_state["winner"] = game_state["board"][combo[0]]
			game_state["scores"][game_state["winner"]] += 1 # Update scores
			return game_state["winner"]
	return None

def make_move(position):
	"""Handles a move and updates the game state."""
	if game_state["board"][position] == " " and game_state["winner"] is None:
		game_state["board"][position] = game_state["current_player"]
		if check_winner():
			return game_state["winner"]
		game_state["current_player"] = "O" if game_state["current_player"] == "X" else "X"
	return None

def get_game_state():
	"""Returns the current game state."""
	return game_state

def reset_game():
	"""Resets the game state and keeps scores."""
	global game_state
	game_state["board"] = [" "] * 9
	game_state["current_player"] = "X"
	game_state["winner"] = None

def reset_scores():
	"""Reset player scores to 0."""
	global game_state
	game_state["scores"] = {"X": 0, "O": 0}

def coin_toss():
	"""Randomly selects a player for the coin toss."""
	return random.choice(["Player 1", "Player 2"])

def set_starting_player(marker):
	"""Set the starting player based on marker choice."""
	global game_state
	game_state["current_player"] = marker