import argparse
from game_suggester.suggester import suggester
from md_to_csv.converter import converter

def main():
	parser = argparse.ArgumentParser(description="Game Suggester")

	group = parser.add_argument_group("Run", "Program to run")
	program_group = group.add_mutually_exclusive_group(required=True)
	program_group.add_argument('--generate', action='store', metavar='path-to-folder-of-md-notes', help='Generate a csv of owned games from a folder of md notes')
	program_group.add_argument('--suggest', action='store', metavar='path-to-csv-of-games', help='Suggest a game from a csv of owned games after answering some questions')

	parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
	args = parser.parse_args()

	if args.generate != None:
		converter(args.generate, args.verbose)
	elif args.suggest != None:
		suggester(args.suggest, args.verbose)
	else:
		# We shouldn't get here
		raise RuntimeError("No valid args provided")

if __name__ == "__main__":
	main()
