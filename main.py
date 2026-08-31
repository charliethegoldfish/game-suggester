import argparse
import sys
from PyQt6.QtWidgets import QApplication
from game_suggester.suggester import suggester
from md_to_csv.converter import converter
from core.main_app import MainApp
from game_suggester.suggester_app import SuggesterApp

def main():
	parser = argparse.ArgumentParser(description="Game Suggester")

	group = parser.add_argument_group("Run", "Program to run")
	program_group = group.add_mutually_exclusive_group()
	program_group.add_argument('--generate', action='store', metavar='path-to-folder-of-md-notes', help='Generate a csv of owned games from a folder of md notes')
	program_group.add_argument('--suggest', action='store', metavar='path-to-csv-of-games', help='Suggest a game from a csv of owned games after answering some questions')

	parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
	args = parser.parse_args()

	if args.generate != None:
		converter(args.generate, args.verbose)
	elif args.suggest != None:
		game_nodes, genres, platforms, status_options, tags = suggester(args.suggest, args.verbose)

		app = QApplication(sys.argv)
		ex = SuggesterApp(game_nodes, genres, platforms, status_options, tags, args.verbose)
		sys.exit(app.exec())
	else:
		if args.verbose:
			print("Running the main app here")

		app = QApplication(sys.argv)
		ex = MainApp(args.verbose)
		sys.exit(app.exec())

if __name__ == "__main__":
	main()
