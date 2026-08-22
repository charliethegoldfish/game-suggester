import yaml
from core.yamlnode import YamlNode

def process_yaml_nodes(nodes: YamlNode, verbose: bool) -> None:
	for node in nodes:
		yaml_dict = yaml.load(node.get_raw_yaml(), Loader=yaml.SafeLoader)
		if verbose:
			print(f'Processing game: "{node.name}"...')
			print(yaml.dump(yaml_dict))