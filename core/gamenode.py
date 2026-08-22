from core.core_config import *
from core.format_functions import format_list_to_str

class GameNode:
	# TODO: This is kinda stupid, maybe there is a better way of setting all this info nicely
	def __init__(self, name: str):
		self.name = name
		self.details = {}
		# self.status = "backlog"
		# self.hours = 0
		# self.platforms = []
		# self.genres = []
		# self.stores = []
		# self.release = None
		# self.related = []
		# self.tags = []

	def set_details(self, details: dict) -> None:
		self.details = details
		# if STATUS_KEY in details:
		# 	self.status = details[STATUS_KEY]

		# if HOURS_KEY in details:
		# 	self.hours = details[HOURS_KEY]

		# if PLATFORMS_KEY in details:
		# 	self.platforms = details[PLATFORMS_KEY]

		# if GENRES_KEY in details:
		# 	self.genres = details[GENRES_KEY]

		# if STORES_KEY in details:
		# 	self.stores = details[STORES_KEY]

		# if RELEASE_KEY in details:
		# 	self.release = details[RELEASE_KEY]

		# if RELATED_KEY in details:
		# 	self.related = details[RELATED_KEY]

		# if TAGS_KEY in details:
		# 	self.tags = details[TAGS_KEY]

	def get_csv_dict(self) -> dict[str, str]:
		csv_dict = {}
		for key in self.details:
			csv_dict[key] = self.details[key]
		csv_dict[NAME_KEY] = self.name
		return csv_dict