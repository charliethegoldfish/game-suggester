import os
from core.gamenode import GameNode
from core.csv_functions import init_csv_dialect
from game_suggester.load_game_functions import load_game_nodes

def suggester(csv_path: str, verbose: bool) -> None:
	
	print("game suggester!")

	try:
		init_csv_dialect()

		abs_csv_path = os.path.abspath(csv_path)
		game_nodes = load_game_nodes(abs_csv_path, verbose)

	except Exception as e:
		print(f'Error suggesting game: {e}')
