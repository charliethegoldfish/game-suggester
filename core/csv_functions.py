import csv
import os
from core.core_config import FIELD_NAMES
from core.gamenode import GameNode

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