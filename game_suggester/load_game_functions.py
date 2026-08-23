from core.gamenode import GameNode
from core.csvnode import CsvNode
from core.csv_functions import csv_to_nodes
from core.core_config import LIST_FIELDS
from core.format_functions import format_str_to_list

def process_csv_node(node: CsvNode, verbose: bool) -> None:
	node_dict = node.get_csv_dict()
	game_details = {}
	for key in node_dict:
		content = node_dict[key]
		if key in LIST_FIELDS:
			content = format_str_to_list(content)
		game_details[key] = content
	if verbose:
		print(f'Setting game details for node: {node.name}')
		# print(game_details)
	node.set_details(game_details)


def load_game_nodes(file_path: str, verbose: bool) -> list[GameNode]:
	csv_nodes = csv_to_nodes(file_path, verbose)

	for node in csv_nodes:
		process_csv_node(node, verbose)

	

	return csv_nodes