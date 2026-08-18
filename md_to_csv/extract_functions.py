import re
from regex_config import YAML_REGEX

def extract_name_from_title(title: str) -> str:
	pass

# functions that process and return properties found in the yaml portion of some md
def extract_genres_from_yaml(yaml: str) -> list[str]:
	pass

def extract_platforms_from_yaml(yaml: str) -> list[str]:
	pass

def extract_stores_from_yaml(yaml: str) -> list[str]:
	pass

def extract_status_from_yaml(yaml: str) -> str:
	pass

def extract_related_games_from_yaml(yaml: str) -> list[str]:
	pass

# generic function to grab the raw str for a given property
def extract_property_raw_from_yaml(yaml: str, property_name: str) -> str:
	pass

def extract_yaml_from_md(markdown: str) -> str:
	yaml = re.search(YAML_REGEX, markdown, flags=re.DOTALL)
	if yaml == None or yaml.group(0) == None:
		return ""
	return yaml.group(0)