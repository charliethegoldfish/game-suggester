def format_content(content: str) -> str:
	formatted = content.lstrip("#") # Get rid of md tag indicators
	formatted = formatted.strip("[]") # Get rid of md note link indicators
	return formatted

def format_list_contents(contents: list[str]) -> list[str]:
	formatted_contents = []
	if contents != None:
		for content in contents:
			content = format_content(content)
			formatted_contents.append(content)
	return formatted_contents

def format_str_to_int(content: str) -> int:
	return int(content)

def format_list_to_str(contents: list[str]) -> str:
	return ','.join(contents)

def format_str_to_list(content: str) -> list[str]:
	return content.split(',')