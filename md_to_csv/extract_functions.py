import re
from md_to_csv.regex_config import YAML_PROPERTIES_REGEX

def extract_name_from_filename(filename: str) -> str:
	return filename.replace(".md", "")

def extract_yaml_from_md(markdown: str) -> str:
	yaml = re.search(YAML_PROPERTIES_REGEX, markdown, flags=re.DOTALL)
	if yaml == None or yaml.group(0) == None:
		return ""
	return yaml.group(0)