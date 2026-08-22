from core.core_config import LIST_FIELDS, NAME_KEY
from core.format_functions import format_list_to_str

class GameNode:
	def __init__(self, name: str):
		self.name = name
		self.details = {}

	def set_details(self, details: dict) -> None:
		self.details = details

	def get_csv_dict(self) -> dict[str, str]:
		csv_dict = {}
		for key in self.details:
			content = self.details[key]
			if key in LIST_FIELDS:
				content = format_list_to_str(content)
			csv_dict[key] = content
		csv_dict[NAME_KEY] = self.name
		return csv_dict