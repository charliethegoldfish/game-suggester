from core.gamenode import GameNode
from core.csvnode import CsvNode
from core.csv_functions import csv_to_nodes
from core.core_config import *
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

def add_list_item(items_to_add: list[str], items: list[str]) -> None:
	for item in items_to_add:
		if item in items or item == '':
			continue
		items.append(item)

def add_item(item: str, items: list[str]) -> None:
	if item in items:
		return
	items.append(item)

def construct_game_library_data(nodes: list[GameNode], platforms: list[str], genres: list[str], status_options: list[str], tags: list[str], verbose: bool) -> dict[str, GameNode]:
	library = {}
	for node in nodes:
		# Create an entry in the game library dict
		library[node.name] = node

		# Add to our list of things if it's not already in there
		add_list_item(node.details[GENRES_KEY], genres)
		add_list_item(node.details[PLATFORMS_KEY], platforms)
		add_item(node.details[STATUS_KEY], status_options)
		add_list_item(node.details[TAGS_KEY], tags)

	return library