from core.core_config import *
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

	# def get_formatted_details(self) -> dict[str, str]:

	def has_platform(self, platform: str) -> bool:
		if platform in self.details[PLATFORMS_KEY]:
			return True
		return False

	def has_status(self, status: str) -> bool:
		return self.details[STATUS_KEY] == status

	def has_any_genres(self, genres: list[str]) -> bool:
		for genre in genres:
			if genre in self.details[GENRES_KEY]:
				return True
		return False

	def has_genre(self, genre: str) -> bool:
		return genre in self.details[GENRES_KEY]

	def has_any_tag(self, tags: list[str]) -> bool:
		for tag in tags:
			if tag in self.details[TAGS_KEY]:
				return True
		return False

	def has_tag(self, tag: str) -> bool:
		return tag in self.details[TAGS_KEY]