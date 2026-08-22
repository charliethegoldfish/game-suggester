import os
from core.yamlnode import YamlNode
from md_to_csv.extract_functions import extract_yaml_from_md, extract_name_from_filename

def create_game_list(folder_path: str, verbose: bool) -> list[YamlNode]:
	# Loop through all the contents of the folder
	items = os.listdir(folder_path)
	nodes = []
	for item in items:
		item_path = os.path.join(folder_path, item)
		if os.path.isfile(item_path) and item.endswith('.md'):
			node = create_game(item, folder_path, verbose)
			nodes.append(node)
	return nodes

def create_game(file: str, folder_path: str, verbose: bool) -> YamlNode:
	file_path = os.path.join(folder_path, file)
	if verbose:
		print(f'Processing file "{file}"...')

	with open(file_path, "r") as f:
		md_content = f.read()
		raw_yaml = extract_yaml_from_md(md_content)
		game_title = extract_name_from_filename(file)
		node = YamlNode(game_title, raw_yaml)
		return node