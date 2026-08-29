import random
from core.gamenode import GameNode

def pick_random_game(games: list[GameNode]) -> GameNode:
	num_games = len(games)
	if num_games <= 0:
		return None
	random_index = random.randint(0, num_games - 1)
	return games[random_index]