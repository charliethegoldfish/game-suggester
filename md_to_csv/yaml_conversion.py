import yaml
from core.yamlnode import YamlNode
from core.core_config import *
from core.format_functions import format_str_to_int, format_list_contents

YAML_TO_NODE_MAPPING = {
	"genre": GENRES_KEY,
	"hours-logged": HOURS_KEY,
	"platform": PLATFORMS_KEY,
	"related-games": RELATED_KEY,
	"released": RELEASE_KEY,
	"status": STATUS_KEY,
	"store": STORES_KEY,
	"tags": TAGS_KEY,
}

YAML_FORMAT_MAPPING = {
	RELATED_KEY: format_list_contents,
	TAGS_KEY: format_list_contents,
}

def process_yaml_nodes(nodes: YamlNode, verbose: bool) -> None:
	for node in nodes:
		yaml_dict = yaml.load(node.get_raw_yaml(), Loader=yaml.SafeLoader)
		if verbose:
			print(f'Processing game: "{node.name}"...')
			# print(yaml.dump(yaml_dict))
			# print(yaml_dict)
		formatted_dict = {}
		for key in yaml_dict:
			if key not in YAML_TO_NODE_MAPPING:
				continue

			new_key = YAML_TO_NODE_MAPPING[key]
			content = yaml_dict[key]

			# Format it if we need to
			if new_key in YAML_FORMAT_MAPPING:
				content = YAML_FORMAT_MAPPING[new_key](content)

			formatted_dict[new_key] = content

		if verbose:
			print(formatted_dict)
		node.set_details(formatted_dict)

