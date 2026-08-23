import csv
import os
from core.core_config import FIELD_NAMES, NAME_KEY
from core.gamenode import GameNode
from core.csvnode import CsvNode

def init_csv_dialect() -> None:
	csv.register_dialect(
		'games-format',
		delimiter=',',
		quotechar='|',
		quoting=csv.QUOTE_MINIMAL,
		escapechar='\\'
	)

def write_to_csv(folder_path: str, file_name: str, game_nodes: list[GameNode]) -> None:
	file_path = os.path.join(folder_path, file_name)
	with open(file_path, 'w', newline='') as csvfile:
		fieldnames = FIELD_NAMES
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect="games-format")

		writer.writeheader()

		for node in game_nodes:
			writer.writerow(node.get_csv_dict())

def csv_to_nodes(file_path: str, verbose: bool) -> list[CsvNode]:
	nodes = []
	# file_path = os.path.join(folder_path, file_name)
	with open(file_path, 'r', newline='') as csvfile:
		reader = csv.DictReader(csvfile, dialect="games-format")
		for row in reader:
			if verbose:
				print(f'Processing game row {row[NAME_KEY]}...')
				# print(row)
			node = CsvNode(row[NAME_KEY], row)
			nodes.append(node)
			
	return nodes
