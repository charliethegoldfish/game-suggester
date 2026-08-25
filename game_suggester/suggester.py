import os
import sys
from PyQt6.QtWidgets import QApplication
from game_suggester.suggester_app import SuggesterApp
from core.gamenode import GameNode
from core.csv_functions import init_csv_dialect
from game_suggester.load_game_functions import load_game_nodes, construct_game_library_data

def suggester(csv_path: str, verbose: bool) -> None:
	
	print("game suggester!")

	try:
		init_csv_dialect()

		abs_csv_path = os.path.abspath(csv_path)
		game_nodes = load_game_nodes(abs_csv_path, verbose)

		genres = []
		platforms = []
		status_options = []
		tags = []

		game_library = construct_game_library_data(game_nodes, platforms, genres, status_options, tags, verbose)

		if verbose:
			print(f'Available platforms: {platforms}')
			print(f'Available genres: {genres}')
			print(f'Available status options: {status_options}')
			print(f'Available tags: {tags}')

		app = QApplication(sys.argv)
		ex = SuggesterApp()
		sys.exit(app.exec())

	except Exception as e:
		print(f'Error suggesting game: {e}')
