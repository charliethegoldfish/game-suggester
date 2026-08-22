import os
from md_to_csv.file_extract_functions import create_game_list
from md_to_csv.yaml_conversion import process_yaml_nodes
from core.yamlnode import YamlNode

# TODO: Have this return a bool as to whether the conversion was successful? 
# And/or return the filepath of the csv output if successful
def converter(folder_path: str, verbose: bool) -> tuple[bool, str|None]:
	print("md to csv converter!")

	try:
		output_folder_path = os.getcwd()
		input_folder_path = os.path.abspath(folder_path)

		if verbose:
			print(f"Output folder: {output_folder_path}")
			print(f"Input folder: {input_folder_path}")

		yaml_nodes = create_game_list(input_folder_path, verbose)
		process_yaml_nodes(yaml_nodes, verbose)

	except Exception as e:
		print(f"Error converting files to csv: {e}")
		return False, None
	